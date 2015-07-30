#!/usr/bin/python

import sys
from service import *
base_dir = "/root/python/github/python/monitor/client"

sys.path.append(base_dir)

enabled_services = {
	'service':(
		('upCheck',upCheckMonitor()),
		('cpu',cpuMonitor()),
	)
}



#print sys.path


