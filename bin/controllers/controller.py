from bin.models import model
from flask import jsonify
import datetime

def verify_email(arg):
	try:
		if arg['rollnumber'] is None or arg['password'] is None:
			return 0
		else:
			verify = arg['db'].execute("SELECT * FROM student WHERE roll_no = %s AND password = %s", (str(arg['rollnumber']),str(arg['password'])))
			result = arg['db'].fetchone()
			if result is None:
				return 0
			else:
				return result[0]
	except Exception as e:
		return str(e)


def feed_menu(args):
	try:
		
		
		for item in args['food']:
			date = item['date']
			food_string = ""
			for food in item['items']:
				print(food)
				food_string = food_string + str(food) + ", "

			query = args['db'].execute("INSERT INTO menu_calendar (date_of_serve,food_items) VALUES (%s,%s)",(str(date),str(food_string[:-2])))
		return 1
	except Exception as e:
		return str(e)

def get_dates(arg):
	try:
		dates = []
		query = arg['db'].execute("SELECT date_of_serve FROM menu_calendar")
		result = arg['db'].fetchall()
		for date in result:
			print(date[0])
			dates.append(datetime.date.isoformat(date[0]))
		return dates
	except Exception as e:
		return str(e)

def get_menu(arg):
	try:
		date = arg['date']
		query = arg['db'].execute("SELECT food_items FROM menu_calendar WHERE date_of_serve = %s",(str(date)))
		result = arg['db'].fetchone()
		print("here")
		if result is None:
			return "Fail"
		else:
			food_items = result[0].split(", ")
			return food_items
	except Exception as e:
		return str(e)

def submit_menu(arg):
	try:
		date = arg['date']
		userid = arg['userid']
		food_menu = arg['food_menu']
		final_menu = ", ".join(food_menu)
		query_verify = arg['db'].execute("SELECT * FROM menu WHERE student_id=%s AND date=%s",(str(userid),str(date)))
		result = arg['db'].fetchone()
		
		if result is not None:
			print(result[0])
			return "Already Filled"
		query = arg['db'].execute("INSERT INTO menu (student_id,date,item) VALUES (%s,%s,%s)",(str(userid),str(date),str(final_menu)))
		return 1
	except Exception as e:
		return str(e)


def verify_admin(arg):
	try:
		if arg['adminid'] is None or arg['password'] is None:
			return 0
		else:
			verify = arg['db'].execute("SELECT * FROM admin WHERE admin_id = %s AND password = %s", (str(arg['adminid']),str(arg['password'])))
			result = arg['db'].fetchone()
			if result is None:
				return 0
			else:
				return result[0]
	except Exception as e:
		return str(e)

def get_students(arg):
	try:
		students = {}
		students['data'] = []
		query = arg['db'].execute("SELECT menu.id,menu.student_id,student.roll_no,student.name,menu.item,menu.verify_status FROM menu JOIN student ON menu.student_id=student.id WHERE menu.date = %s",(str(arg['date'])))
		result = arg['db'].fetchall()
		for student in result:
			temp = {}
			# temp.append(student[0])
			# temp.append(student[2])
			# temp.append(student[3])
			# temp.append(student[4])
			temp['id'] = student[0]
			# temp['student_id'] = student[1]
			temp['rollnumber'] = student[2]
			temp['name'] = student[3]
			temp['item'] = student[4]
			if student[5] == 0:
				temp['verify'] = '<a href=#><button id='+str(student[2])+' class="btn btn-primary verify_btn" data-id='+str(student[0])+' data-name='+str(student[3])+' data-rollnumber='+str(student[2])+' data-date='+str(arg['date'])+'>Verify</button></a>'
				# temp['edit'] = 	'<a href=#><button id='+str(student[0])+str(student[2])+' class="btn btn-primary verify_btn" data-id='+str(student[0])+' data-name='+str(student[3])+' data-rollnumber='+str(student[2])+' data-date='+str(arg['date'])+'>Edit</button></a>'
			else:
				temp['verify'] = "Verified"
				# temp['edit'] = "Verified"
			students['data'].append(temp)
		return jsonify(students)
	except Exception as e:
		return jsonify(str(e))

def verify_student(arg):
	try:
		query = arg['db'].execute("UPDATE menu SET verify_status = 1 WHERE id=%s",(str(arg['id'])))
		if query:
			return "Success"
		else:
			return "Fail"
	except Exception as e:
		return str(e)