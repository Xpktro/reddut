from django.conf.urls import patterns, url
from redditApp import views
from redditApp.views.generic import LinkDetailView


urlpatterns = patterns('',
    url(
        r'^$',
        views.index,
        name="reddit_index",
    ),

    url(
        r'^(?P<pk>\d+)/$',
        LinkDetailView.as_view(),
        name="reddit_link",
    ),

    url(
        r'^(?P<pk>\d+)/comment/$',
        views.comment,
        name="reddit_comment",
    ),

    url(
        r'^(?P<link_id>\d+)/comment/vote/(?P<way>(up|down))/(?P<comment>\d+)/$',
        views.vote_comment,
        name="reddit_vote_comment",
    ),

    url(
        r'^(?P<link_id>\d+)/vote/(?P<way>(up|down))/(?P<next>(i|l))/$',
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

    url(
        r'^register/$',
        views.register,
        name="reddit_register",
    )
)
