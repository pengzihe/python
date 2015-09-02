from django.shortcuts import render, render_to_response
from django.contrib import auth,comments
from django.contrib.auth.models import User
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
	return render_to_response("index.html",{'user':request.user,'page':'index'})

def linux_bbs(request):
	return render_to_response("bbs_list.html",{'content':"Linux bbs page!",'user':request.user,'page':'linux'})

def python_bbs(request):
	bbs_list = bbs.objects.filter(category='python')
	return render_to_response("bbs_list.html",{'user':request.user,'bbs_list':bbs_list,'page':'python'})

def login(request):
	return render_to_response("login.htm")

def login_auth(request):
	print request.POST
        username,password = request.POST['username'],request.POST['password']
        user = auth.authenticate(username = username,password = password)
        print '+++++',user
        if user is not None:  #authentications is correct
                auth.login(request,user)
                return HttpResponseRedirect('/')
        else:
                return render_to_response("login.htm",{'login_err':"Wrong username or password!"})
		


def logout(request):
	#c_user = request.user
	auth.logout(request)
	return HttpResponse("user %s has logged out, <a href='/login/'> please click to re_login</a>" % request.user)



	#return HttpResponse(request.POST)



def bbs_detail(request,bbs_id):
	bbs_obj = bbs.objects.get(id=bbs_id)
	print '*'*30, bbs_obj
	return render_to_response("bbs_detail.html",{'bbs_obj':bbs_obj})

def article(request):
	return render_to_response("create_article.html")


def submit_article(request):
	bbs_title =  request.POST.get('bbs_title')
	bbs_content = request.POST.get('bbs_content')
	bbs_category = request.POST.get('bbs_category')
	bbs.objects.create(
		title = bbs_title,
		content = bbs_content,
		category = bbs_category,
		author = User.objects.get(id = request.user.id),
		publish_date = datetime.datetime.now(),
		modify_date = datetime.datetime.now()
	)
	return HttpResponse('yes')

def sub_comment(request):
	content_type = 7
	bbs_id = request.GET.get('bbs_id')
	comment = request.GET.get('text')
	sub_date = datetime.datetime.now()
	
	c = comments.Comment.objects.create(
		content_type_id = content_type,
		object_pk = bbs_id,
		site_id = 1,
		user_id = request.user.id,
		comment = comment,
		submit_date = sub_date,
	)
	c.save()
	return HttpResponseRedirect("/detail/%s/" % bbs_id)

