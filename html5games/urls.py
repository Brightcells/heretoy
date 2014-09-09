# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls import patterns, include, url

urlpatterns = patterns('html5games.views',
    url(r'^$', 'home', name='home'),
    url(r'^play/(?P<pk>\d+)/$', 'play', name='play'),
    url(r'^share/(?P<pk>[^/]+)$', 'share', name='share'),
    url(r'^share/(?P<pk>[^/]+)/$', 'share', name='share'),
    url(r'^share/wap/(?P<pk>\d+)/$', 'wap_share', name='wap_share'),
    url(r'^share/pc/(?P<pk>\d+)/$', 'pc_share', name='pc_share'),
)
