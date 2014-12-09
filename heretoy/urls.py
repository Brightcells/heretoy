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
    url(r'^status/', 'heretoy.views.status', name='status'),
)

urlpatterns += patterns('games_bak.views',
    url(r'^inverter/', 'inverter', name='inverter'),
    url(r'^inverter2/', 'inverter2', name='inverter2'),
    url(r'^colornot/', 'colornot', name='colornot'),
    url(r'^airplane/', 'airplane', name='airplane'),
    url(r'^FarmInvaders/', 'FarmInvaders', name='FarmInvaders'),
    url(r'^JumpingThief/', 'Jumping', name='Jumping'),
    url(r'^yzdmx/', 'yzdmx', name='yzdmx'),

    # url(r'^cogames/58kdxyx/', 'kdxyx', name='58kdxyx'),
    # url(r'^cogames/58aydzz/', 'aydzz', name='58aydzz'),
    url(r'^cogames/58kdxyx/', 'offline', name='58kdxyx'),
    url(r'^cogames/58aydzz/', 'offline', name='58aydzz'),
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

urlpatterns += staticfiles_urlpatterns('static')

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
