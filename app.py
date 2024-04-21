from flask import Flask, render_template, redirect, url_for, request
from flask_mysqldb import MySQL
import os


app = Flask(__name__)

app.secret_key = 'key'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL-PASSWORD'] = ''
app.config['MYSQL_DB'] = 'test'

mysql = MySQL(app)

# @app.route('/')
# def index():
#     cur = mysql.connection.cursor()
#     cur.execute("SELECT * FROM ecommerce timed")
#     data = cur.fetchall()
#     cur.execute("SELECT COUNT(*) FROM ecommerce timed")
#     admin_count = cur.fetchone()[0]
#     teacher_count = cur.fetchone()[0]
#     student_count = cur.fetchone()[0]
#     cur.close()
#     return render_template('index.html', data=data, admin_count=admin_count, teacher_count=teacher_count, student_count=student_count)

@app.route('/')
def admin():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM ecommerce")
    data = cur.fetchall()
    cur.execute("SELECT COUNT(*) FROM ecommerce")
    admin_count = cur.fetchone()[0]
    cur.close()
    return render_template('admin.html', data=data, admin_count=admin_count)

@app.route('/teacher')
def teacher():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM timed")
    data = cur.fetchall()
    cur.execute("SELECT COUNT(*) FROM timed")
    teacher_count = cur.fetchone()[0]
    cur.close()
    return render_template('teacher.html', data=data, teacher_count=teacher_count)

@app.route('/student')
def student():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM timed")
    data = cur.fetchall()
    cur.execute("SELECT COUNT(*) FROM timed")
    student_count = cur.fetchone()[0]
    cur.close()
    return render_template('student.html', data=data, student_count=student_count)

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' in request.files:
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file,filename)
            return 'file uploaded seccessfully'
        return 'File upload failed'
    return render_template('file-upload.html')
    
def allowed_file(filename):
    return'.' in filename and filename.rsplict('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if '__main__' == __name__:
    app.run(debug=True)