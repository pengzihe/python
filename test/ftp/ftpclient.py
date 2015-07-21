#!/usr/bin/env python


import socket,tab,time

HOST='172.16.20.210'
PORT=50001
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))

def usage():
	print """
		help    
		get   get file from FTP server
		put   send file to FTP server
		ls    show file list on FTP server
		quit  exit
	"""
	

while True:
	msg = raw_input("ftp> ")
	if len(msg)==0:continue
	#s.sendall(msg)
	#data = s.recv(4096)
	#print data
	elif msg == "?" or msg =="help":
		usage()
	elif msg == "ls" or msg.split()[0] == "get" or msg.split()[0] == "put":
		s.sendall(msg)
        	data = s.recv(4096)
        	print data
		if data == 'ReadyToReceiveFile':
			with open(msg.split()[1]) as f:
				s.sendall(f.read())
				time.sleep(0.5)
				print "Transfer is done.."
				s.send('SendIsDone')	
		elif data == 'ReadyToSendFile':
			print msg.split()[1]
			f = file('get/%s' % msg.split()[1],'wb')
			while True:
				data = s.recv(4096)
                		if data == "SendSuccess":
              	        		print "Download is done.. ", msg.split()[1]
                                	break
                        	f.write(data)
                        	f.flush()
               	 	f.close()
	elif msg == "quit":break
	else:
		print "The command is error,please view the help file: "
		usage()
						
	#print 'Received', data

s.close()
