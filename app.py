from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_mysqldb import MySQL
import pandas as pd
import os
import openpyxl


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

@app.route('/upload')
def upload():
    return render_template('upload.html')

# @app.route('/view', methods=['POST'])
# def view():
#     file = request.files['file']
#     file.save(file.filename)
#     data = pd.read_excel(file)
#     return data.to_html()


@app.route('/view', methods=['GET','POST'])
def view():
    if request.method==['POST']:
        file = request.file['file']
        wb = openpyxl.load_workbook(file)
        sheet = wb.active
        cursor = mysql.connection.cursor()
        for row in sheet.filter_rows(values_only=True):
            cursor.execute("INSERT INTO ecommerce (username, email,password) VALUES(%s,%s,%s)",row)
            mysql.connection.commit()
            return jsonify({'message': 'Data Uploaded Successfully'})
        return render_template('upload.html')
    


# @app.route('/', methods=['GET', 'POST'])
# def upload():
#     if request.method == 'POST':
#         file = request.files['file']

#         upload=upload(filename=file.filename, data=file.read())
#         db.session.add(upload)
#         db.session.commit()

#         return f'Uplaodded: {file.filename}'
#     return render_template('file_upload.html')

# @app.route('/upload', methods=['POST'])
# def file_upload():
#     if 'file' in request.files:
#         file = request.files['file']
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file,filename)
#             return 'file uploaded seccessfully'
#         return 'File upload failed'
#     return render_template('upload-file.html')
    
# def allowed_file(filename):
#     return'.' in filename and filename.rsplict('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if '__main__' == __name__:
    app.run(debug=True)