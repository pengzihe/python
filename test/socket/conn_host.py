#!/usr/bin/python

import pxssh,host_info

def connectHost(command):
	try:
		HInfo = host_info.hostInfo()
		host = HInfo.hostInfo()
		for i in host:
        		s = pxssh.pxssh()
       	 		s.login(i[1],i[2],i[3])
        		s.sendline(command)
        		s.prompt()
        		print s.before
			s.logout()
	except pxssh.ExceptionPxssh,e:
       		print "pxssh failed on login."
       		print str(e)


connectHost('pwd')
