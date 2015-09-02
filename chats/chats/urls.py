from django.conf.urls import patterns, include, url

from django.contrib import admin
from chat01.views import *

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chats.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',index),
    url(r'^room_num/(\d+)/',room_num),
    url(r'^login/$',login),
    url(r'^login_auth/$',login_auth),
    url(r'^getMsg/$',getMsg),
)
