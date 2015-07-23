#!/usr/bin/python

import pxssh,host_info,time,threading,pexpect

class execute:
	def __connectHost(self,command,hostname,ip,username,password):
		try:
        		s = pxssh.pxssh()
       			s.login(ip,username,password)
        		s.sendline(command)
        		s.prompt()
        		print "\n-------------------------------%s----------------------------------\n%s\n%s" % (hostname,s.before,time.ctime())
			s.logout()
		except pxssh.ExceptionPxssh,e:
       			print "pxssh failed on login."
       			print str(e)


	def run(self,cmd,sql):
		print time.ctime()
		HInfo = host_info.hostInfo()
		host = HInfo.hostInfo(sql)
		for i in host:
			#print i
			t = threading.Thread(target=self.__connectHost,args=(cmd,i[0],i[1],i[2],i[3],))
			t.start()
		print "current has %d threads" % (threading.activeCount() - 1)

	def __connectScp(self,hostname,ip,username,password,filename,pathname):
		child = pexpect.spawn('/usr/bin/scp',[filename,username+'@'+ip+':'+pathname])
		try:
        		child.expect('(?i)password:')
        		child.sendline(password)
        		child.expect(pexpect.EOF)
        		print "\n-------------------------------%s----------------------------------\n%s\n%s" % (hostname,child.before,time.ctime())
		except EOF:
        		print "EOF error."
		except TIMEOUT:
        		print "Timeout error"
	
	def scp(self,filename,sql,pathname='/root'):
		print time.ctime()
		HInfo = host_info.hostInfo()
		host = HInfo.hostInfo(sql)
		for i in host:
			t = threading.Thread(target=self.__connectScp,args=(i[0],i[1],i[2],i[3],filename,pathname,))
			t.start()
		print "current has %d threads" % (threading.activeCount() - 1)


if __name__ == "__main__":
	r = execute()
	r.run('date',"select * from host where hostname='test_www'")
	#r.scp('menu.py',"select * from host where hostname='test_pay'")
