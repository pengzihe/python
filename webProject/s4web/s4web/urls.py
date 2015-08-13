from django.conf.urls import patterns, include, url

from django.contrib import admin

from app01.views import *
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 's4web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
       (r'^sayhi/$','app01.views.hello'),
       (r'^second/$',second),
       (r'^time/plus/(\d+)/','app01.views.plus_hour'),
	(r'^$',index),
	(r'^linux/$',linux_bbs),
	(r'^python/$',python_bbs),
	(r'^login_auth/$',login_auth),
	(r'^login/$',login)
)
