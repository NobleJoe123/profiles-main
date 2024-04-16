from flask import Flask, render_template
from flask_mysqldb import MySQL


app = Flask(__name__)

app.secret_key = 'key'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL-PASSWORD'] = ''
app.config['MYSQL_DB'] = 'test'

mysql = MySQL(app)

@app.route('/')
def admin():
    return render_template('admin.html')

@app.route('/teachers')
def teachers():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM timed")
    data = cur.fetchall()
    cur.close()
    return render_template('teacher.html', data=data)


if '__main__' == __name__:
    app.run(debug=True)