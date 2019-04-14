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