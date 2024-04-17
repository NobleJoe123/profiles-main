from flask import Flask, render_template, redirect, url_for
from flask_mysqldb import MySQL


app = Flask(__name__)

app.secret_key = 'key'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL-PASSWORD'] = ''
app.config['MYSQL_DB'] = 'test'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin')
def admin():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM ecommerce")
    data = cur.fetchall()
    cur.close()
    return render_template('admin.html', data=data)

@app.route('/teacher')
def teacher():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM timed")
    data = cur.fetchall()
    cur.close()
    return render_template('teacher.html', data=data)

@app.route('/student')
def student():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM timed")
    data = cur.fetchall()
    cur.close()
    return render_template('student.html', data=data)

if '__main__' == __name__:
    app.run(debug=True)