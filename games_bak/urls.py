# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('games_bak.views',
    url(r'^bindphone/(?P<cash>\d+)/$', 'bind_phone', name='bindphone'),
    url(r'^getcash/(?P<cash>\d+)/$', 'get_cash', name='getcash'),
    url(r'^share/(?P<cash>\d+)/$', 'share', name='share'),
    url(r'^retry/$', 'retry', name='retry'),
    url(r'^refresh/$', 'refresh', name='refresh'),
)
