# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('data.views',
    url(r'^games$', 'games', name='games'),
    url(r'^games/$', 'games', name='games'),
    url(r'^play/$', 'play', name='play'),
    url(r'^like/$', 'like', name='like'),
    url(r'^unlike/$', 'unlike', name='unlike'),
    url(r'^plu$', 'plu', name='plu'),
    url(r'^plu/$', 'plu', name='plu'),
    url(r'^mine$', 'mine', name='mine'),
    url(r'^mine/$', 'mine', name='mine'),
    url(r'^nail$', 'nail', name='nail'),
    url(r'^nail/$', 'nail', name='nail'),
    url(r'^favorite$', 'favorite', name='favorite'),
    url(r'^favorite/$', 'favorite', name='favorite'),
    url(r'^topic/(?P<tp>[^/]+)$', 'topic', name='topic'),
    url(r'^topic/(?P<tp>[^/]+)/$', 'topic', name='topic'),
    url(r'^lunbotu/$', 'lunbotu', name='lunbotu'),
)
