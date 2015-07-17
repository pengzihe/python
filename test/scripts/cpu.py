#!/usr/bin/python
import commands
def cpuMonitor():
	cmd = "sar  1 1 | tail -n 1 | awk '{print $5,$6,$8}'"
	status,result = commands.getstatusoutput(cmd)
	return result,status
