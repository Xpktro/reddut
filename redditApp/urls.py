from django.conf.urls import patterns, url

urlpatterns = patterns('redditApp.views',
    url(r'^$', 'index'),
    url(r'^(?P<link_id>\d+)/$', 'link'),
    url(r'^(?P<link_id>\d+)/vote/(?P<way>(up|down))/$', 'vote'),
    url(r'^submit/$', 'submit'),
)