from django.conf.urls import patterns, include, url

urlpatterns = patterns('accounts.views',
    # url(r'^change_user/$', 'change_user', name='change_user'),
    url(r'^signup/$', 'user_signup', name='user_signup'),
    url(r'^login/$', 'user_login', name='user_login'),
    url(r'^logout/$', 'user_logout', name='user_logout'),
)
