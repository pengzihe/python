#!/usr/bin/python
import menu,host_info,conn_host

def machine(value):
	HInfo = host_info.hostInfo()
	if value == 'host' or value == 'view':
		host = HInfo.hostInfo()
	elif value == 'group':
		host = HInfo.hostInfo("select distinct groupname from groups")  
	print "\n----------------------------%s list----------------------------\n" % value
	for i in host:
	#	print "\t", i[0]
		if value == 'group':
			gInfo = host_info.hostInfo()
			sql = "select hostname from host where hostname = any(select hostname from groups where groupname = '%s')" % i[0]
			g =  gInfo.hostInfo(sql)
			print '\n\tGroup\t\t\tHost'
			
			print "\t", i[0]
			for i in g:
				print '\t\t\t\t',i[0]
		else:
			
			print "\t", i[0]
	if value == 'view':
		print "\n"
		return 0
	ChooseHost = raw_input("\nPlease input you want to choose: ")
	
	return ChooseHost
		


def BeSure(hostname,choose):
	HInfo = host_info.hostInfo()
	run = conn_host.execute()
	subMenu = menu.subTitle()
	null = 0
	if choose == 1:
        	host = HInfo.hostInfo()
		sql = "select * from host where hostname = '%s'" % hostname
	elif choose == 2:
		host = HInfo.hostInfo("select distinct groupname from groups")
		sql = "select * from host where hostname = any(select hostname from groups where groupname = '%s')" % hostname
	for i in host:
		if i[0] == hostname:
			null = 1
			if subMenu == '1':	
				cmd = raw_input("Please input you need to run command or input 'quit' will exit: ")
				if cmd == 'quit':return 0
				run.run(cmd,sql)
			elif subMenu == '2':
				filename = raw_input("Please input you need to copy of the file name or input 'quit' will exit: ")
				if filename == 'quit':return 0
				pathname = raw_input("Please input you need to save path or input 'quit' will exit: ")
				run.scp(filename,sql,pathname)
			elif subMenu == '3':break
			
	if null == 0:
		print "The %s is absent." % hostname


m = menu.title()

while True:
	if m == '1':
		h = machine('host')
		BeSure(h,1)
		break
	elif m == '2':
		h = machine('group')
		BeSure(h,2)
		break
	elif m == '3':
		machine('view')
		break
	elif m == '4':
		break
	else:
		m = menu.title()
