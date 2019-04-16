#!/usr/bin/env python3

from flask import Flask,render_template,jsonify,request,session,redirect
from flaskext.mysql import MySQL
import config
from bin.controllers import controller



app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
mysql = MySQL(app)
app.secret_key = 'd!pr@m!t'
conn = mysql.connect()
conn.autocommit(True)
cursor = conn.cursor()

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/student')
def student_page():
	if 'id' in session:
		dates = controller.get_dates({'db':cursor})
		verify_email = session['id']
		return render_template('student_dates.html',verify_email=verify_email,dates=dates)
	return render_template('student_login.html')

@app.route('/student/login', methods=['POST'])
def student_login():
	# print(request.form['rollnumber'])
	rollnumber = request.form['rollnumber']
	password = request.form['password']
	verify_email = controller.verify_email({'rollnumber':rollnumber,'password':password, 'db':cursor})
	print(verify_email)
	dates = controller.get_dates({'db':cursor})
	if verify_email:
		session['id'] = verify_email
	return render_template('student_dates.html',verify_email=verify_email,dates=dates)



@app.route('/admin')
def admin_page():
	if 'adminid' in session:
		dates = controller.get_dates({'db':cursor})
		verify_admin = session['adminid']
		return render_template('admin_dates.html',verify_email=verify_admin,dates=dates)
	return render_template('admin_login.html')


@app.route('/feed_menu',methods=['POST'])
def feed_menu():
	args = request.get_json(force=True)
	arg = {}
	arg['food'] = args['calendar']
	arg['db'] = cursor
	feeder = controller.feed_menu(arg)
	if feeder == 1:
		return "Success"
	else:
		return feeder

@app.route('/get_menu',methods=['POST'])
def get_menu():
	if 'id' not in session:
		return redirect('/')
	arg = {}
	arg['date'] = request.form['dateselect']
	# arg['date'] = '2019-04-14'
	arg['db'] = cursor
	food_menu = controller.get_menu(arg)
	if type(food_menu) == str:
		return food_menu
	else:
		print("asdad")
		print(food_menu)
		return render_template('student_dashboard.html',food_menu = food_menu,date=arg['date'])


@app.route('/submit_meal',methods=['POST'])
def submit_meal():
	if 'id' not in session:
		return redirect('/')
	arg = {}
	arg['date'] = request.form['date']
	arg['food_menu'] = request.form.getlist('food_menu')
	arg['userid'] = session['id']
	arg['db'] = cursor
	print(arg)
	feed_menu = controller.submit_menu(arg)
	return render_template('student_submission.html',feed_menu = feed_menu)

@app.route('/student/logout',methods=['GET'])
def student_logout():
	if 'id' not in session:
		return redirect('/')
	else:
		session.pop('id',None)
		return redirect('/')

@app.route('/admin/logout',methods=['GET'])
def admin_logout():
	if 'adminid' not in session:
		return redirect('/')
	else:
		session.pop('adminid',None)
		return redirect('/')

@app.route('/admin/login',methods=['POST'])
def admin_login():
	adminid = request.form['adminid']
	password = request.form['password']
	verify_admin = controller.verify_admin({'adminid':adminid,'password':password, 'db':cursor})
	# print(verify_admin)
	dates = controller.get_dates({'db':cursor})
	# if verify_email:
	session['adminid'] = verify_admin
	return render_template('admin_dates.html',verify_email=verify_admin,dates=dates)
	
@app.route('/admin/dashboard',methods=['POST'])
def admin_dashboard():
	if 'adminid' not in session:
		return redirect('/')
	date = request.form['dateselect']
	session['date'] = date
	return render_template('admin_dashboard.html',date=date)

@app.route('/admin/get_students',methods=['GET'])
def get_students():
	# arg = request.get_json(force=True)
	date = session['date']
	session.pop('date',None)
	return controller.get_students({'db':cursor,'date':date})

@app.route('/admin/verify_student',methods=['POST'])
def verify_student():
	arg = request.get_json(force=True)
	print(arg)
	id = arg['id']
	return controller.verify_student({'db':cursor,'id':id})

# App run in debug mode, False for production mode.
if __name__ == '__main__':
	app.run()
