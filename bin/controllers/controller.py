from bin.models import model
from flask import jsonify

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
				return 1
	except Exception as e:
		return str(e)