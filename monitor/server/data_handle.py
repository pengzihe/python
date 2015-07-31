#!/usr/bin/python

import socket
HOST = '0.0.0.0'
PORT = 50000

def send_status_data(action,status_data):  #action:differentiate type  status_data:send values

        #send monitor data to server side

        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((HOST,PORT))

        #user_input = "test data...."
        if action == 'PushDataIntoRedis':
                s.send('PushDataIntoRedis')
                server_confirmation = s.recv(1024)
                if server_confirmation == 'PushedDataIntoRedis':
                        print "------connecting redis to pull out of data----"

        #print "sending...." 
        data = s.recv(1024)
        print data
        s.close()
send_status_data('PushDataIntoRedis','')
