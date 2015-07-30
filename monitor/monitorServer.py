#!/usr/bin/python

import SocketServer,time,json

class MyTCPHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		print 'got a connection from: ', self.client_address[0]
		data_type = self.request.recv(1024)
		if data_type == "SendMonitorData":
			print 'send back confirmation signal'
			self.request.send('ReadyToReceive')
			status_data = self.request.recv(8192)
			print status_data
		


if __name__ == "__main__":
	HOST = ""
	PORT = 50000
	server = SocketServer.ThreadingTCPServer((HOST,PORT),MyTCPHandler)


server.serve_forever()


