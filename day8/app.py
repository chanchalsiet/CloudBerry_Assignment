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
    
    """https://github.com/chanchalsiet/CloudBerry_Assignment/tree/main/day8"""
"""Http error Codes :
                200 --Succuess -- Request was successful
                201 --Created – A new resource was created (e.g., feedback submitted).
                204 --No Content – Request successful, but no response body.
                400 --Bad request --Request has invalid syntax
                401 --Unauthorized access --Client need to authorize the request
                403 --Forbidden --Client dosent have the access to access the request
                404 --Page not found -- Page not found
                408 -- Request timed out ---Session timed out waiting for the request
                500 --Internal server Error --Server is in unexpected condition to  process the request
                502,504 -- Bad Gateway ---Got a invalid response from the upstream server
                503 -- Service unavailable --- Server is not in responding to fulfill the request
"""
