from flask import Flask, render_template, request
import sqlite3
app = Flask(__name__)


connection = sqlite3.connect('database.db')
print('DATABASE CONNECTED')

connection.execute('CREATE TABLE IF NOT EXISTS posts (title TEXT, post TEXT)')
print('TABLE CREATED')

connection.close()


@app.route('/')
def home():
    return 'Dobro Dosli!'

@app.route('/new')
def newPost():
    return render_template('home.html')

@app.route('/addrecord', methods=['POST'])
def addrecord():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    try:
        title = request.form['title']
        post = request.form['post']
        cursor.execute('INSERT INTO posts (title, post) VALUES (?, ?)' , (title, post))
        connection.commit()
        message = 'SUCCESS!!!'
    except:
        connection.rollback()
        message = 'ERROR ERROR'
    finally:
        return render_template('result.html', message = message)
        conneciton.close()
