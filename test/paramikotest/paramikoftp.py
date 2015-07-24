#!/usr/bin/python
import paramiko,sys,os
host = sys.argv[1]
user = 'root'
password = 'www.eegoo'
cmd = sys.argv[2]

s = paramiko.SSHClient()   
s.load_system_host_keys()  
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())  

t = paramiko.Transport((host,22))
t.connect(username=user,password=password)


sftp = paramiko.SFTPClient.from_transport(t)
#sftp.get(cmd,'di.txt')
sftp.put(cmd,'/tmp/di.txt')

s.close()  
