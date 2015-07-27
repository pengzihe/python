#!/usr/bin/python

import os,sys

msg = """

Welcome using mico's auditing system!
"""
print msg


host_dic = {
	'mico':('172.16.20.52','root','p','www.eegoo'),
	'steven':('172.16.20.210','root','p','www.eegoo'),
}

while True:
	for hostname,ip in host_dic.items():
		print hostname,ip
	try:
		host = raw_input('\nPlease choose one server to login: ').strip()
	except KeyboardInterrupt:
		continue
	except EOFError:
		continue
	if len(host) == 0:continue
	elif not host_dic.has_key(host):continue
	print host_dic[host][0],host_dic[host][1],host_dic[host][2],host_dic[host][3]
	os.system('python demo.py %s %s %s %s' %(host_dic[host][0],host_dic[host][1],host_dic[host][2],host_dic[host][3]))
	break
