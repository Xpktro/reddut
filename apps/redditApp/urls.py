from django.conf.urls import patterns, url
from django.views.generic import DetailView
from redditApp import views
from redditApp.models import Link

urlpatterns = patterns('',
    url(
        r'^$',
        views.index,
        name="reddit_index",
    ),

    url(
        r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Link,
            context_object_name="link",
            template_name="myreddit/link.html",
        ),
        name="reddit_link",
    ),


    url(
        r'^(?P<link_id>\d+)/vote/(?P<way>(up|down))/$',
        views.vote,
        name="reddit_vote",
    ),

    url(
        r'^submit/$',
        views.submit,
        name="reddit_submit",
    ),

    url(
        r'^login/$',
        views.login_view,
        name="reddit_login",
    ),

    url(
        r'^logout/$',
        views.logout_view,
        name="reddit_logout",
    ),
)
