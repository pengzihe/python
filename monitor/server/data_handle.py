#!/usr/bin/python

from conf.templates import enabled_templates
#print enabled_templates

from get_monitor_index_dic import monitor_host_dic
import socket,time,json
import redis_connector as redis
HOST = '0.0.0.0'
PORT = 50000

def send_status_data(action,status_data):  #action:differentiate type  status_data:send values

        #send monitor data to server side

        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((HOST,PORT))

	status_dic = None
        #user_input = "test data...."
        if action == 'PushDataIntoRedis':
                s.send('PushDataIntoRedis')
                server_confirmation = s.recv(1024)
                if server_confirmation == 'PushedDataIntoRedis':
                        print "------connecting redis to pull out of data----"
			status_dic = redis.r.get('STATUS_DATA')
			

        #print "sending...." 
       # data = s.recv(1024)
        #print data
        s.close()
	return status_dic
while True:
	latest_status_dic = send_status_data('PushDataIntoRedis','')
	if latest_status_dic is not None:
		latest_status_dic = json.loads(latest_status_dic)
		for h,t_list in monitor_host_dic.items():
			print h,t_list
			if latest_status_dic.has_key(h):
				print latest_status_dic[h]
			else:
				print "no valid data from %s in DB" % h
	else:
		print "------------error-------------"


	time.sleep(10)
