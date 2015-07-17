#!/usr/bin/python


def countNum():
	for i in range(10):
		yield i

a = countNum()
print a.next()
print a.next()
print a.next()
print a.next()
print a.next()
