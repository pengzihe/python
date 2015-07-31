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
		
	}
