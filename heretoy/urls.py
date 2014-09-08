from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chongxiaomi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^diorsclubadmin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    url(r'^', include('html5games.urls', namespace='html5games')),
    url(r'^data/', include('data.urls', namespace='data')),
    url(r'^cxxdr/', include('eatshit.urls', namespace='eatshit')),

    # url(r'^download/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.DOWNLOADS_ROOT, 'show_indexes':True}),
)

urlpatterns += patterns('',
    url(r'^inverter/', 'games_bak.views.inverter', name='inverter'),
    url(r'^inverter2/', 'games_bak.views.inverter2', name='inverter2'),
)

urlpatterns += staticfiles_urlpatterns('static')

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
