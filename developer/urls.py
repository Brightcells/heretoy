from django.conf.urls import patterns, include, url

urlpatterns = patterns('developer.views',
    url(r'^submit/$', 'submit_game', name='submit_game'),
    url(r'^edit/(?P<md5>\w+)/$', 'edit_game', name='edit_game'),
    url(r'^update/(?P<md5>\w+)/$', 'update_game', name='update_game'),
    url(r'^games/$', 'games', name='games'),
)
