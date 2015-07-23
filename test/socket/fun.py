#!/usr/bin/python
import menu,host_info,conn_host



def input(rawsInput,listName):
	  while True:
                rawInput = raw_input(rawsInput).strip()
                if rawInput in listName:
                        return rawInput
                elif rawInput == 'quit':
                        return 'quit'
                elif len(rawInput) == 0: continue
                else:
                        print "The '%s' is no exist,please input agait." % rawInput


def machine(value):            ##define host and group info.
	HInfo = host_info.hostInfo()
	machineInfo = []
	if value == 'host' or value == 'view':
		host = HInfo.hostInfo()
	elif value == 'group':
		host = HInfo.hostInfo("select distinct groupname from groups")  
	print "\n----------------------------%s list----------------------------\n" % value
	for i in host:
                machineInfo.append(i[0])
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
	print "\n"
	if value == 'view':
		print "\n"
		return 0
	ChooseInfo = "Please input you want to choose or input 'quit' will exit: "
 	return input(ChooseInfo,machineInfo)	

		


def BeSure(name,choose):   ## choose hosts or groups execute commands.
	HInfo = host_info.hostInfo()
	run = conn_host.execute()
	subTitle = ['Execute commands', 'Copy Files','Exit']
	subMenu = menu.title(subTitle)
	null = 0
	if choose == 1:
        	host = HInfo.hostInfo()
		sql = "select * from host where hostname = '%s'" % name
	elif choose == 2:
		host = HInfo.hostInfo("select distinct groupname from groups")
		sql = "select * from host where hostname = any(select hostname from groups where groupname = '%s')" % name
	for i in host:
		if i[0] == name:
			null = 1
			if subMenu == '1':	
				cmd = raw_input("Please input you need to run command or input 'quit' will exit: ")
				if cmd == 'quit':return 0
				run.run(cmd,sql)
			elif subMenu == '2':
				filename = raw_input("Please input you need to copy of the file name or input 'quit' will exit: ")
				if filename == 'quit':return 0
				pathname = raw_input("Please input you need to save path or input 'quit' will exit: ")
				if pathname == 'quit':return 0
				run.scp(filename,sql,pathname)
			elif subMenu == '3':break
			
	if null == 0:
		print "The %s is absent." % name


def nameInfo(sql):  ##check group or hostname info
	HInfo = host_info.hostInfo()
        groups = HInfo.hostInfo(sql)
	groupInfo = []
	for i in groups:
		groupInfo.append(i[0])
	return groupInfo

def addInfo():  ##add hosts or groups info.
	HInfo = host_info.hostInfo()
        addSQLCommands = HInfo.hostInfo()
	title_name = ['Add host', 'Add group','Del host','Del group','Host added to group','Exit']
	v = menu.title(title_name)
	if v == '1':
		addHostHostname = raw_input("Please input you want to add Host's hostname: ").strip()
		addHostIp = raw_input("Please input you want to add Host's ip address: ").strip()
		addHostUsername = raw_input("Please input you want to add Host's username: ").strip()
		addHostPassword = raw_input("Please input you want to add Host's password: ").strip()
		sql = "insert into host values('%s','%s','%s','%s')" %(addHostHostname,addHostIp,addHostUsername,addHostPassword)
		addSQLCommands = HInfo.hostInfo(sql)
		if addSQLCommands == 0:
			print "Add '%s' host is failed." % addHostHostname
		else:	
			print "Add '%s' host is successful." % addHostHostname
	elif v == '2':
		while True:
			
			addGroupname = raw_input("Please input you want to add Group's groupname or input 'quit' will exit: ").strip()
			sql = "select distinct groupname from groups"
			if addGroupname in nameInfo(sql):
                        	print "The '%s' group is exist,add failed and please input groupname again." % addGroupname
				continue
			elif len(addGroupname) == 0:continue
			elif addGroupname == 'quit':break
			sql = "insert into groups (groupname) values('%s')" % addGroupname
			addSQLCommands = HInfo.hostInfo(sql)
			if addSQLCommands == 0:
                        	print "Add '%s' group is failed." % addGroupname
                	else:
                        	print "Add '%s' group is successful." % addGroupname
	elif v == '3':
		while True:
			delHost = "Please input you need to delete hostname or input 'quit' will exit: "
			sql = "select hostname from host"
			result = input(delHost,nameInfo(sql))
			if result == 'quit':return 0
			sql = "delete from host where hostname='%s'" % result
                	addSQLCommands = HInfo.hostInfo(sql)
                	if addSQLCommands == 0:
                		print "Delete '%s' host is failed." % result
                	else:
               	        	print "Delete '%s' host is successful." % result
				
	elif v == '4':
		while True:
			delGroup = "Please input you need to delete groupname or input 'quit' will exit: "
			sql = "select groupname from groups"
			result = input(delGroup,nameInfo(sql))
			if result == 'quit':return 0
			sql = "delete from groups where groupname='%s'" % result
                	addSQLCommands = HInfo.hostInfo(sql)
                	if addSQLCommands == 0:
                		print "Delete '%s' host is failed." % result
                	else:
               	        	print "Delete '%s' host is successful." % result
	
	elif v == '5':
		sql = "select hostname from host"
		h = nameInfo(sql)
		print '-----------------------------------------------------------------The host list----------------------------------------------------------------------------'
                print '|\t%s\t|' %('\t|\t'.join(h))
		print '----------------------------------------------------------------------------------------------------------------------------------------------------------\n'
		hostName = "Please input you need to  added hostname to group: "
		hostNameValue = input(hostName,h)
		if hostNameValue == 'quit':return 0


		sql = "select distinct groupname from groups"
		g = nameInfo(sql)
		print '-----------------------------------------------------------------The group list----------------------------------------------------------------------------'
                print '|\t%s\t|' %('\t|\t'.join(g))
		print '-----------------------------------------------------------------------------------------------------------------------------------------------------------\n'
		groupName = "Please input your groupname: "
		groupNameValue = input(groupName,g)
		if groupNameValue == 'quit':return 0
		
		checkSql = "select hostname from groups where hostname='%s' and groupname='%s'" % (hostNameValue,groupNameValue)
		checkName = nameInfo(checkSql)

		if hostNameValue in checkName:
			print "The '%s' host already in '%s' group,No added." % (hostNameValue,groupNameValue)
			return 0


		sql = "insert into groups values('%s','%s')" % (groupNameValue,hostNameValue)
                addSQLCommands = HInfo.hostInfo(sql)
                if addSQLCommands == 0:
                	print "The '%s' host added to %s group is failed." % (hostNameValue,groupNameValue)
                else:
                	print "The '%s' host added to %s group is successful." % (hostNameValue,groupNameValue)



	elif v == '6':return 0
	
	


def runMenu():  ##define the main program
	title_name = ['Choose the host', 'Choose the group','View all hosts','Added(Delete) info(Host or group)','Exit']
	m = menu.title(title_name)

	while True:
		if m == '1':
			h = machine('host')
			if h == 'quit':break
			BeSure(h,1)
			break
		elif m == '2':
			h = machine('group')
			if h == 'quit':break
			BeSure(h,2)
			break
		elif m == '3':
			machine('view')
			break
		elif m == '4':
			addInfo()
			break
		elif m == '5':
			break
		else:
			m = menu.title(title_name)

runMenu()
