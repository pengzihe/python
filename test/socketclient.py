#!/usr/bin/env python


import socket

HOST='172.16.20.210'
PORT=50030
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))

while True:
	msg = raw_input("Please input your msg: ")
	if len(msg)==0:continue
	s.sendall(msg)
	data = s.recv(1024)
	print 'Received', data

s.close()
