#!/usr/bin/python

def deco( f):
	#def pack():
	def pack(*args, **kwargs):
		print "Going to virify if you are valid user!"
		f(*args,**kwargs)
		print "I am finished....welcome"
	return pack

@deco
def sayHi():
	print "Hello, i am mico."


@deco
def sayName(name):
	print "Hello,I am %s ------" % name

@deco
def sayAge(name,age):
	print "Hello,I am %s and i am %s years old." % (name,age)

sayHi()
print "\n"
sayName('mico')
print "\n"
sayAge('steven',10)
