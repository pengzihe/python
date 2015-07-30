#!/usr/bin/env python
import conf
from plugins import cpu,upCheck

class MonitorBase:
	interval = 300
	plugin = None

class upCheckMonitor(MonitorBase):
	interval = 10
	plugin = upCheck

class cpuMonitor(MonitorBase):
	interval = 15
	plugin = cpu
	
