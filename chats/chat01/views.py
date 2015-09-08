from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from chat01.models import *
from django.contrib import auth
import time,json
# Create your views here.


#global msg_dic

msg_dic = {}

#generate a room_msg_dic for each chat room.
for room in chatRoom.objects.all():
	msg_dic[room.id] = {
        	'msg_num':0,
        	'msgs':[]
	}




def login(request):
	return render_to_response('login.html')

def index(request):
	rooms = chatRoom.objects.all()
	return render_to_response("index.html",
		{'rooms':rooms,'user':request.user}
	)

@login_required
def room_num(request,room_id):
	print 'room id', room_id
	room_obj = chatRoom.objects.get(id = room_id)
	return render_to_response('chat_room.html',{'user':request.user,'room_obj':room_obj})


def login_auth(request):
        username,password = request.POST['username'],request.POST['password']
        user = auth.authenticate(username = username,password = password)
        if user is not None:  #authentications is correct
                auth.login(request,user)
		return HttpResponseRedirect('/')
        else:
                return render_to_response("login.html",{'login_err':"Wrong username or password!"})

def getMsg(request):
	#print request.GET
	username,msg = request.GET.get('user'),request.GET.get('msg')	
	cur_time = time.strftime('%Y_%m_%d %H:%M:%S')
	room_id = int(request.GET.get('room_id'))
	print "room_id",room_id
	msg_dic[room_id]['msgs'].append((cur_time,username,msg))
	msg_dic[room_id]['msg_num'] += 1
	print msg_dic
	return HttpResponse('message is ok!')

def pushMsg(request):  #send all message to client
	client_msg_id = int(request.GET.get('msg_id'))
	client_room_id = int(request.GET.get('room_id'))
	print 'msg_id:',client_msg_id
	new_msg_num = client_msg_id - msg_dic[client_room_id]['msg_num']
	if client_msg_id == 0:
		msg_list = msg_dic[client_room_id]['msgs'][-5:]
	elif new_msg_num == 0:
		msg_list = []
	else:
		msg_list = msg_dic[client_room_id]['msgs'][new_msg_num:]	

	print new_msg_num,'*'*20
	new_msgs = {
		'msgs':msg_list,
		'msg_num':msg_dic[client_room_id]['msg_num']
	}
	return HttpResponse(json.dumps(new_msgs))


def getMembers(request):
	print request.GET
	room_id = request.GET.get('room_id')
	member_list = chatAccount.objects.filter(rooms = room_id)
	member_dic = {}
	for u in member_list.select_related():
		member_dic[u.user.username] = [u.user.username,u.user.id]
	print member_dic
	return HttpResponse(json.dumps(member_dic))	
	
