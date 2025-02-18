
#Create a new Flask page with a form that asks for a user’s name and displays a greeting
from flask import Flask, redirect, url_for, request,render_template
app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('home.html')
@app.route('/login', methods=['GET'])
def login():
    if request.method == 'GET':
        user = request.args.get('fname')
        return 'Welcome %s' % user
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

