# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('games_bak.views',
    # url(r'^bindphone/(?P<cash>\d+)/$', 'bind_phone', name='bindphone'),
    # url(r'^getcash/(?P<cash>\d+)/$', 'get_cash', name='getcash'),
    url(r'^bindphone/(?P<cash>\d+)/$', 'offline', name='bindphone'),
    url(r'^getcash/(?P<cash>\d+)/$', 'offline', name='getcash'),
    url(r'^share/(?P<cash>\d+)/$', 'share', name='share'),
    url(r'^offline/$', 'offline', name='offline'),
    url(r'^retry/$', 'retry', name='retry'),
    url(r'^count/$', 'count', name='count'),
    url(r'^refresh/$', 'refresh', name='refresh'),
)
