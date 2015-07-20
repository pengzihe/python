#!/usr/bin/env python

import socket
import commands

HOST=''
PORT=50000
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)

while True:
	conn,addr = s.accept()
	print 'Connected by', addr
	while True:
	
		data = conn.recv(1024)
		if not data:break
		print 'going to run cmd:', data
		status,result = commands.getstatusoutput(data)	
		if len(result) == 0: result ="CMD executed."
		conn.sendall("Server: %s" % result)

conn.close()

