#!/usr/bin/env python3

from flask import Flask,render_template,jsonify,request
from flaskext.mysql import MySQL
import config
from bin.controllers import controller



app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
mysql = MySQL(app)
conn = mysql.connect()
conn.autocommit(True)
cursor = conn.cursor()

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/student')
def student_page():
	return render_template('student_login.html')

@app.route('/student/login', methods=['POST'])
def student_login():
	# print(request.form['rollnumber'])
	rollnumber = request.form['rollnumber']
	password = request.form['password']
	verify_email = controller.verify_email({'rollnumber':rollnumber,'password':password, 'db':cursor})
	print(verify_email)
	if verify_email:
		return "Sucess"
	else:
		return "Fail"



@app.route('/admin')
def admin_page():
	return render_template('admin_login.html')





# App run in debug mode, False for production mode.
if __name__ == '__main__':
	app.run()
