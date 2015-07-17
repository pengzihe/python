#!/usr/bin/python




checkInList = []
student_id_list ={1:'jake'}

class school:
	school_name = "Mico Linux training center"
	address = "Bujie Longgang District,Shenzhen China."
	phone = '0755-28262222'
	teachers = ['Mico','Steven']
	def registration(self,s_name):
		latest_id = max(student_id_list.keys())
		s_id = latest_id + 1
		student_id_list[s_id] = s_name

class student(school):
	def __init__(self,name):
		self.name = name

	def CheckIn(self,time):
		if time < 931:
			print "%s check in.." % self.name
			return self.name
		else:
			print "%s check in is late." % self.name

	def tuition(self):
			print "%s paied tution." % self.name

s1 = student('mico')
s2 = student('steven')
s3 = student('zero')

time = 929
for i in s1,s2,s3:
	checkIn = i.CheckIn(time)
	if checkIn is not None:
		checkInList.append(checkIn)
		time += 1
	i.registration(i.name)
	
print checkInList
print student_id_list
		
