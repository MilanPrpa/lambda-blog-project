from flask import Flask, render_template, request
import sqlite3
app = Flask(__name__)

connection = sqlite3.connect('database.db')
print('DATABASE CONNECTED')

connection.execute('CREATE TABLE IF NOT EXISTS posts(title TEXT, post TEXT)')
print('TABLE CREATED')

connection.close()


@app.route('/')
def homePage():
    return 'Welcome!!'

@app.route('/new')
def newPost():
    return render_template('home.html')

@app.route('/addrecord', methods = ['POST'])
def addRecord():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    try:
        title = request.form['title']
        post = request.form['post']
        cursor.execute('INSERT INTO posts(title, post) VALUES (?, ?)', (title, post))
        connection.commit()
        message = 'it worked'
    except:
        connection.rollback()
        message = 'error'
    finally:
        return render_template('result.html', message = message)
        connection.close()




    app.run(debug = True)
