#!/usr/bin/python

class Dog:
	def __init__(self,name,age=18):
		self.name = name
		self.age = age
	def bulk(self):
		print "hehehehe....,my name is %s, i am %s years old." % (self.name,self.age)

	def __auth(self):
		print "cannot be called outside of this class." 

	def eat(self,food):
		print "i like eat %s." % food
		self.__auth()
	
d = Dog('Sam')
d.bulk()
d.eat('meat')
