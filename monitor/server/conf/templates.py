#!/usr/bin/python

class BaseTemplate:
	name = None
	groups = []
	hosts = []
	service_dic = {}
	
class LinuxGenericServices(BaseTemplate):
	name = 'Linux Generic Services'
	groups = ['BJ']
	hosts = ['zero']
	service_dic = {
		'cpu':
		'upCheck':
	}
