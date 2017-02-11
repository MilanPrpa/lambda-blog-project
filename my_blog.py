from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def greet():
    return render_template('home.html')

@app.route('/birthday')
def bday():
    return 'August 5th 1979'

@app.route('/greeting/<name>')
def greeting(name):
    return 'Hello %s' % 'Milan'
