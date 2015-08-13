from django.shortcuts import render, render_to_response
from django.contrib import auth
# Create your views here.
from app01.models import *


from django.http import HttpResponse,HttpResponseRedirect
import datetime

def hello(request):
	ct = datetime.datetime.now()
	name_list = ['mico','zero','steven']
	for i in range(20):name_list.append(i)
	return render_to_response("hello.html",{'key':ct,'name_info':name_list})

def second(request):

	return HttpResponse( datetime.datetime.now())


def plus_hour(request,hour):
	ct = datetime.datetime.now()
	h = int(hour)
	dt = ct + datetime.timedelta(hours = h)
	return HttpResponse('Current Time plus %s <br/> The new time: %s' % (ct,dt))

def index(request):
	#print "-------------",request.user
	return render_to_response("index.html",{'user':request.user})

def linux_bbs(request):
	return render_to_response("bbs_list.html",{'content':"Linux bbs page!",'user':request.user})

def python_bbs(request):
	bbs_list = bbs.objects.filter(category='python')
	return render_to_response("bbs_list.html",{'user':request.user,'bbs_list':bbs_list,})

def login(request):
	return render_to_response("login.htm")

def login_auth(request):
	print request.POST
	username,password = request.POST['username'],request.POST['passwd']
	user = auth.authenticate(username = username,password = password)
	print '+++++',user
	if user is not None:  #authentications is correct
		auth.login(request,user)
		return HttpResponseRedirect('/')
	else:
		return render_to_response("login.htm",{'login_err':"Wrong username or password!"})

		




	#return HttpResponse(request.POST)
