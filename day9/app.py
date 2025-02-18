from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = "secret"

tasks = []

@app.route('/')
def home():
    return render_template('index.html', tasks = tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    due_date = request.form.get('due_date')
    if task and due_date:  # Highlighted change
        tasks.append({'task': task, 'completed': False, 'due_date': due_date})  # Highlighted change
        flash('Task added successfully', 'success')
    return redirect('/')

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if task_id < len(tasks):
        tasks.pop(task_id)
        flash('Task deleted successfully', 'danger')
    return redirect('/')

@app.route('/mark_as_complete/<int:task_id>')
def mark_as_complete(task_id):
    if task_id < len(tasks):
        tasks[task_id]["completed"] = True
        flash('Task completed successfully', 'success')
    return redirect('/')

@app.route('/delete_all')
def delete_all():
    tasks.clear()
    flash('Task deleted successfully', 'danger')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)