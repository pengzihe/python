#!/usr/bin/python

import MySQLdb


class hostInfo:
	def hostInfo(self,statement="select * from host"):
		try:
			conn = MySQLdb.connect(host='localhost',user='root',passwd='123456',db='socket',port=3306)
			cur = conn.cursor()
			cur.execute(statement)
			result = []
			for line in cur.fetchall():
				 result.append(line)
			cur.close()
			conn.commit()
			conn.close()
			return result
		except MySQLdb.Error,e:
			return 0
			print "Mysql Error msg: ",e
#a = hostInfo()
#b = "insert into host values('a','127.0.0.1','root','123')"
#print  a.hostInfo()
#for i in c:
#	print i[0]


