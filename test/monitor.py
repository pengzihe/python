#!/usr/bin/env python
from servicemodel import *
class defaultModel:
	hostname = None
	ip_address = None
	customized_services = None
	monitor_service = [cpus,'memory','load','network']
	graph_list = ['cpu','memory']


class host1(defaultModel):
	hostname = 'mico'
	ip_address = '172.16.20.51'
	customized_services  = [cpus,'mysql']

class host2(defaultModel):
	hostname = 'steven'
	ip_address = '172.16.20.52'
	customized_services  = [cpus,'apache']
	#customized_services[0].interval = 500

class host3(defaultModel):
	hostname = 'python'
	ip_address = '172.16.20.510'

	customized_services  = [cpus,'apache']


enabled_monitors = (
	host1(),
	host2(),
	host3()
)

for i in enabled_monitors:
#	print i.hostname,i.ip_address,
	c =  i.monitor_service[0]
	print c
	print c.interval
	print c.index_dic
	print c.script
	print "--------------------------"
