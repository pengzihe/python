#!/usr/bin/python

from multiprocessing import Process,Pool
import time
def sayHi(n):
	print "Hello, my name is %s ,how are you ?" % n
	time.sleep(2)

pool = Pool(processes = 50)


pool.map(sayHi,range(100))
"""
result = []
for i in range(1000):
	#p = pool.apply_async(sayHi,[i])
	result.append(pool.apply_async(sayHi,[i]))


for i in result:
	i.get()
"""
