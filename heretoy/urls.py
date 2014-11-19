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
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
)

urlpatterns += patterns('',
    url(r'^', include('html5games.urls', namespace='html5games')),
    url(r'^data/', include('data.urls', namespace='data')),
    url(r'^cogames/', include('cogames.urls', namespace='cogames')),
    url(r'^games_bak/', include('games_bak.urls', namespace='games_bak')),
    url(r'^developer/', include('developer.urls', namespace='developer')),

    url(r'^cxxdr/', include('eatshit.urls', namespace='eatshit')),

    # url(r'^download/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.DOWNLOADS_ROOT, 'show_indexes':True}),
)

urlpatterns += patterns('',
    url(r'^inverter/', 'games_bak.views.inverter', name='inverter'),
    url(r'^inverter2/', 'games_bak.views.inverter2', name='inverter2'),
    url(r'^colornot/', 'games_bak.views.colornot', name='colornot'),
    url(r'^airplane/', 'games_bak.views.airplane', name='airplane'),
    url(r'^FarmInvaders/', 'games_bak.views.FarmInvaders', name='FarmInvaders'),
    url(r'^JumpingThief/', 'games_bak.views.Jumping', name='Jumping'),
    url(r'^yzdmx/', 'games_bak.views.yzdmx', name='yzdmx'),

    url(r'^58kdxyx/', 'games_bak.views.kdxyx', name='58kdxyx'),
    url(r'^58aydzz/', 'games_bak.views.aydzz', name='58aydzz'),
)

urlpatterns += staticfiles_urlpatterns('static')

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
