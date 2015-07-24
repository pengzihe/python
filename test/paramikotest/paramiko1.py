#!/usr/bin/python
import paramiko,sys,os
host = sys.argv[1]
user = 'root'
password = 'www.eegoo'
cmd = sys.argv[2]

s = paramiko.SSHClient()   
s.load_system_host_keys()  
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())  

s.connect(host,22,user,password,timeout=5)  
stdin,stdout,stderr = s.exec_command(cmd)  
cmd_result = stdout.read(),stderr.read()  

for line in cmd_result:   
	print line,    

s.close()  
