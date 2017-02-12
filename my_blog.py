from flask import Flask
app = Flask(__name__)

@app.route('/')
def intro():
    return 'Hello, and welcome to my page on this little thing called the internet'

@app.route('/birthday')
def myBday():
    return 'I was born August 5th, 1979'

@app.route('/greeting/<user>')
def greeting(user):
    return 'Hello %s' %('Milan')
