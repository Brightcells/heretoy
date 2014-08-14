# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('eatshit.views',
    url(r'^$', 'home', name='home'),
    url(r'^cxxdr/(?P<name>[^/]+)/$', 'eatshit', name='eatshit'),
    url(r'^share/(?P<name>[^/]+)/$', 'share', name='share'),
)
