from django.shortcuts import render, render_to_response

# Create your views here.

from django.http import HttpResponse
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
