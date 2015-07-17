#!/usr/bin/python

import MySQLdb

try:
	conn = MySQLdb.connect(host='localhost',user='root',passwd='123456',db='python',port=3306)   #连接数据库
	cur = conn.cursor()  ##cursor用来执行命令的方法，光标
	cur.execute("insert into host_list values('py','172.16.20.55','windows')")
	cur.execute('select * from host_list')  ##执行单条语句
	for line in cur.fetchall():  ##接收全部的返回结果行
		print line
	cur.close()   #关闭光标
	conn.commit()  ##提交事务，否则插入的数据不会保存到mysql中
	conn.close()  #关闭数据库连接
	
except MySQLdb.Error,e:
	print "Mysql Error Msg:",e
