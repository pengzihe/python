#!/usr/bin/python
from conf.hosts import group_dic
import SocketServer,time,json,sys
import redis_connector as redis

host_dic = {}
for group,host_list in group_dic.items():
	for h_name,h_info in host_list.items():
		host_dic[h_name] = {}
	

#print host_dic
#sys.exit()
class MyTCPHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		print 'got a connection from: ', self.client_address[0]
		data_type = self.request.recv(1024)
		if data_type == "SendMonitorData":
			print 'send back confirmation signal'
			self.request.send('ReadyToReceive')
			status_data = json.loads(self.request.recv(8192))
			if host_dic.has_key(status_data['hostname']):
				host_dic[status_data['hostname']] = status_data
		elif data_type == "PushDataIntoRedis":
			print "----------going to save data into redis....done!"
			redis.r['STATUS_DATA'] = json.dumps(host_dic)
			self.request.send('PushedDataIntoRedis')
			
			#print status_data
		#for host,info in host_dic.items():
		#	print info
		print host_dic
		


if __name__ == "__main__":
	HOST = ""
	PORT = 50000
	server = SocketServer.ThreadingTCPServer((HOST,PORT),MyTCPHandler)


server.serve_forever()


