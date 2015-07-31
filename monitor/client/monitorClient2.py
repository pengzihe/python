#!/usr/bin/python
from conf.conf import *
import socket,tab,time,json
HOST = '0.0.0.0'
PORT = 50000
monitor_dic = {}

hostname = 'mico'

def send_status_data(action,status_data):  #action:differentiate type  status_data:send values

	#send monitor data to server side

	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect((HOST,PORT))

	#user_input = "test data...."
	if action == 'SendMonitorData':
		s.send('SendMonitorData')
		server_confirmation = s.recv(1024)
		if server_confirmation == 'ReadyToReceive':
			s.sendall(status_data)

	#print "sending...." 
	data = s.recv(1024)
	print data
	s.close()



for k,v in enabled_services.items():
	if k == "service":
		for (s_name, service_api) in v:
			monitor_dic[s_name] = {'last_check': 0, 
						'interval': service_api.interval,
						'plugin': service_api}
			#print s_name
			#print service_api.plugin.monitor()
#print monitor_dic
while True:
	status_dic = { 'hostname':hostname }
	for service_name,value_dic in monitor_dic.items():
#		print service_name
		#print value_dic['last_check'] + value_dic['interval'] - time.time()

		# The means you need to trigger the next round.
		if time.time() - value_dic['last_check'] >= value_dic['interval']:  
			value_dic['last_check'] = time.time() #put the latest time stamp into monitor dic
		
			status_dic[service_name] = value_dic['plugin'].plugin.monitor()
	#		print status_dic[service_name] 
			print "\033[42;1mnext round for:\033[0m", service_name
		if len(status_dic) > 1:
			send_status_data('SendMonitorData',json.dumps(status_dic)) #use json.dumps by the dic become string format transfer to monitor server.
			print '------------- sending status data to monitor server -------------'
			"""
			for k,v in status_dic.items():
				print k
				if k != 'hostname':
					for index,values in v.items():
						print "\t",index,values
			"""
		
	time.sleep(2)	

	#break
	

