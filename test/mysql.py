#!/usr/bin/python

import MySQLdb

try:
	conn = MySQLdb.connect(host='localhost',user='root',passwd='123456',db='python',port=3306)   
	cur = conn.cursor()  
	#cur.execute("insert into host_list values('py','172.16.20.55','windows')")
	cur.execute('select * from host_list')  
	"""for line in cur.fetchall(): 
		print line
	v_list = []
	for i in range(10):
		v_list.append(("TestServer%s" %i ,"172.16.20.5%s" %i ,"CentOS"))
	print v_list
	cur.executemany("insert into host_list values(%s,%s,%s)" , v_list)"""
	cur.scroll(4,mode="relative")
	print cur.fetchone()
	cur.close()   
	conn.commit() 
	conn.close()  
	
except MySQLdb.Error,e:
	print "Mysql Error Msg:",e
