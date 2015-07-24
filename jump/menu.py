#!/usr/bin/python

import os,sys

msg = """

Welcome using mico's auditing system!
"""
print msg


host_dic = {
	'mico':'172.16.20.52',
	'steven':'172.16.20.210',
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
	os.system('python demo.py %s' % host_dic[host])
	break
