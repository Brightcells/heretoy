# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('eatshit.views',
    url(r'^$', 'home', name='home'),
    url(r'^eatshit/(?P<pk>\d+)/$', 'eatshit', name='eatshit'),
    url(r'^share$', 'share', name='share'),
)
