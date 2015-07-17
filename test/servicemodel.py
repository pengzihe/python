#!/usr/bin/python
from scripts import cpu
#print cpu.status
class serviceModel:
	interval = 300
	retry = 3
	alert_amount = 5 
	graph_list = None


class cpus(serviceModel):
	index_dic = {
		'idle':[20,10],
		'system':[80,90],
		'iowait':[50,70],
	}
	graph_list = ['idle','iowait']
	script = cpu.cpuMonitor()
