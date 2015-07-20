#!/usr/bin/python


import SocketServer

class MyTCPHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		print "got a connection from: ",self.client_address[0]
		while True:
			self.data = self.request.recv(1024).strip()
			if not self.data:
				print "Client is disconnected..",self.client_address[0]
				break
			print self.data
			self.request.sendall(self.data.upper())



if __name__ == "__main__":
	HOST,PORT = '0.0.0.0',50001
	server = SocketServer.ThreadingTCPServer((HOST,PORT),MyTCPHandler)


server.serve_forever()

