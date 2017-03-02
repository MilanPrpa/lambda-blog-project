from flask import Flask, render_template, request, jsonify
import sqlite3
app = Flask(__name__)


connection = sqlite3.connect('database.db')
print('CONNECTED DATABASE')

connection.execute('CREATE TABLE IF NOT EXISTS friends (name TEXT, age INTEGER)')
print('CREATED TABLE')

connection.close()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/newfriend', methods=['POST'])
def newFriend():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()


    try:
        name = request.form['name']
        age = request.form['age']
        cursor.execute('INSERT INTO friends (name, age) VALUES (?, ?)', (name, age))
        connection.commit()
        message = 'SUCCESS'
    except:
        connection.rollback()
        message = 'An error occured'
    finally:
        return render_template('result.html', message = message)
        connection.close()

@app.route('/friends')
def friends():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM friends')
    friendsList = cursor.fetchall()
    connection.close()
    return jsonify(friendsList)



    app.run(debug = True)
