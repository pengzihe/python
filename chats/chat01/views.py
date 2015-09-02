from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, render_to_response
from chat01.models import *
from django.contrib import auth
# Create your views here.


def login(request):
	return render_to_response('login.html')

def index(request):
	rooms = chatRoom.objects.all()
	return render_to_response("index.html",
		{'rooms':rooms,'user':request.user}
	)

def room_num(request,room_id):
	print 'room id', room_id
	return render_to_response('chat_room.html',{'user':request.user})


def login_auth(request):
        username,password = request.POST['username'],request.POST['password']
        user = auth.authenticate(username = username,password = password)
        if user is not None:  #authentications is correct
                auth.login(request,user)
		return HttpResponseRedirect('/')
        else:
                return render_to_response("login.html",{'login_err':"Wrong username or password!"})

def getMsg(request):
	print request.GET	
	return HttpResponse('message is ok!')
