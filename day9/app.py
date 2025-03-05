from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
# from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Change for MySQL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret'  # Required for Flash messages
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# 🔹 Define User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    task = db.Column(db.String(200), nullable=False)
    due_date = db.Column(db.String(20), nullable=False)
    completed = db.Column(db.Boolean, default=False)

    user = db.relationship('User', backref=db.backref('tasks', lazy=True))
# def __repr__(self):
#         return f'<Task {self.task}>'
# 🔹 Create Tables Before First Request
with app.app_context():
    db.create_all()

# tasks = []
@app.route('/')
def home():
    return redirect(url_for('login'))
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Check if the user exists in DB
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            session['user_id'] = user.id
            flash("Login successful!", "success")
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid credentials, try again!", "danger")

    return render_template('login_page.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if username already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists! Try another.', 'danger')
            return redirect(url_for('signup'))

        # Hash the password before storing
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash('User registered successfully!', 'success')
        return redirect(url_for('login'))

    return render_template('signup.html')


# 🔹 Dashboard Route (Protected)
@app.route('/dashboard')
def dashboard():
    user = User.query.get(session['user_id'])  # Get current user
    tasks = Task.query.filter_by(user_id=user.id).all()  # Fetch tasks for logged-in user
    return render_template('task_detail.html', user=user, tasks=tasks)
    #return render_template('task_detail.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)  # Remove user session
    session.pop('username', None)
    session.clear()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('login'))

def task_detail():
    return render_template('task_detail.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    # task = request.form.get('task')
    # due_date = request.form.get('due_date')
    task_name = request.form['task']
    due_date = request.form['due_date']

    # Convert due_date string to datetime.date object
    try:
        due_date = datetime.strptime(due_date, "%Y-%m-%d").date()
    except ValueError:
        flash("Invalid date format!", "danger")
        return redirect(url_for('dashboard'))

    new_task = Task(task=task_name, due_date=due_date, user_id=session['user_id'])

    db.session.add(new_task)
    db.session.commit()
    user = User.query.get(session['user_id'])  # Get current user
    tasks = Task.query.filter_by(user_id=user.id).all()  # Fetch tasks for logged-in user
    flash('Task added successfully', 'success')
    return render_template('task_detail.html', user=user, tasks=tasks)
    # # flash("Task added successfully!", "success")
    # user = User.query.get(session['user_id'])  # Get current user
    # tasks = Task.query.filter_by(user_id=user.id).all()  # Fetch tasks for logged-in user
    # # if task_name and due_date:  # Highlighted change
    # #     tasks.append({'task': task_name, 'completed': False, 'due_date': due_date})  # Highlighted change
    # flash('Task added successfully', 'success')
    # return render_template('task_detail.html', tasks=tasks)

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    task = Task.query.get(task_id)
    print(task)
    if task:
        db.session.delete(task)
        db.session.commit()
        flash("Task deleted successfully!", "success")
    else:
        flash("Task not found!", "danger")
    user = User.query.get(session['user_id'])  # Get current user
    tasks = Task.query.filter_by(user_id=user.id).all()  # Fetch tasks for logged-in user
    return render_template('task_detail.html', user=user, tasks=tasks)

@app.route('/mark_as_complete/<int:task_id>', methods=['GET'])
def mark_as_complete(task_id):
    task = Task.query.get(task_id)
    if task:
        task.completed = True  # ✅ Mark as completed
        db.session.commit()
        flash("Task marked as completed!", "success")
    else:
        flash("Task not found!", "danger")

    user = User.query.get(session['user_id'])  # Get current user
    tasks = Task.query.filter_by(user_id=user.id).all()  # Fetch tasks for logged-in user
    return render_template('task_detail.html', tasks=tasks)

@app.route('/delete_all')
def delete_all():
    tasks.clear()
    flash('Task deleted successfully', 'danger')
    return render_template('task_detail.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)