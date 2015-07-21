#!/usr/bin/python


import SocketServer,time,commands

class MyTCPHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		print "got a connection from: ",self.client_address[0]
		while True:
			self.data = self.request.recv(1024).strip()
			if not self.data:
				print "Client is disconnected..",self.client_address[0]
				break
			
			if self.data.split()[0] == 'ls':
				status,result = commands.getstatusoutput(self.data.split()[0])
				self.request.sendall(result)
			elif self.data.split()[0] == 'put':
				print "Going to receive file ", self.data.split()[1]

				f = file('put/%s' % self.data.split()[1],'wb')
				self.request.sendall("ReadyToReceiveFile")

				while True:
					data = self.request.recv(4096)
					if data == "SendIsDone":
						print "Transfer is done.."
						break
					f.write(data)	
					f.flush()
				f.close()
			elif self.data.split()[0] == 'get':
				print "Going to send file ", self.data.split()[1]
				self.request.sendall("ReadyToSendFile")
				time.sleep(0.5)
				with open(self.data.split()[1]) as f:
					self.request.sendall(f.read())
					time.sleep(0.5)
					print "Sending is done.."
					self.request.send("SendSuccess")

if __name__ == "__main__":
	HOST,PORT = '0.0.0.0',50001
	server = SocketServer.ThreadingTCPServer((HOST,PORT),MyTCPHandler)


server.serve_forever()

