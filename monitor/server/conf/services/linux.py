#!/usr/bin/python

from generic import DefaultService



class upCheck(DefaultService):
	name = 'upCheck'
	interval = 30
	monitor_dic = {
			'host_status': [None]
	}

class cpu(DefaultService):
	name = 'cpu'
	interval = 60
	monitor_dic =	{
		'idle':['percentage',20,5],
		'iowait':['percentage',40,60],
		'system':['percentage',80,90]
		
	}
	lt_operator = ['idle']
