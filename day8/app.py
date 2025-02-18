from flask import Flask, render_template, request, flash, redirect, jsonify

app = Flask(__name__)
app.secret_key = "supersecretkey"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html', name='John Doe', fact ='I am a web developer')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    if request.method == 'POST':
        name = request.form['name']
        return render_template('greet.html', name=name)
    return render_template('form.html')

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        feedback = request.form.get('feedback')
        flash(f"Feedback submitted successfully: {feedback}", "success")
        #  redirect
        return redirect('/feedback')
    return render_template('feedback.html')

@app.route('/api/data')
def get_data():
    return jsonify({'name': 'John Doe', 'age': 30})


if __name__ == '__main__':
    app.run(debug=True)