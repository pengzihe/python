#!/usr/bin/python

from multiprocessing import Process,Manager
import time


global name_list
name_list = []

def sayHi(m,name,n):
	time.sleep(2)
	print "Hello, my name is %s, how are you ?" % name,n
	m.append(n)
	#print m

manager = Manager()
l = manager.list()
for i in range(10):
	p = Process(target=sayHi,args=(l,'mico',i,))
	p.start()
	p.join()


print l
