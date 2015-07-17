#!/usr/bin/python

while True:
	try:
		int(raw_input("Please input your age: "))
		a =['mico','steven']
		if 'jake' not in a:raise IOError
		break
	except ValueError:
		print "You must input an integer."

	except:
		print "unexcepted error,please contact us."
	
