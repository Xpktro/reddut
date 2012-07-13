from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(
        r'^myreddit/',
        include('redditApp.urls'),
        name="reddit_root",
    ),

    url(
        r'^$',
        RedirectView.as_view(
            url="/myreddit/",
            permanent=True,
        )
    ),
)
