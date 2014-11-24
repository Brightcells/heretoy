# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('cogames.views',
    url(r'^yiguan_koudai4/$', 'yiguankoudai', name='yiguankoudai'),
    url(r'^yiguan_koudai2/$', 'yiguankoudai2', name='yiguankoudai2'),
    url(r'^yiguan_koudai3/$', 'yiguankoudai3', name='yiguankoudai3'),
    url(r'^yiguan_koudai/$', 'yiguankoudai4', name='yiguankoudai4'),
)
