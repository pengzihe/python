#!/usr/bin/python

from services import linux
class BaseTemplate:
	name = None
	groups = []
	hosts = []
	service_dic = {}
	
class LinuxGenericServices(BaseTemplate):
	name = 'Linux Generic Services'
	groups = ['BJ','HK']
	hosts = ['zero']
	service_dic = {
		'cpu': linux.cpu(),
		'upCheck':linux.upCheck(),
	}

class WindowsGenericServices(BaseTemplate):
	name = 'Windows Generic Services'
	groups = ['HK']
	service_dic = {
		'upCheck':linux.upCheck(),
	}

enabled_templates = (
	LinuxGenericServices(),
	WindowsGenericServices(),
)

