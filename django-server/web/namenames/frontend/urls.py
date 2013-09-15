from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#
# Import class based views
#
import namenames.frontend.views
from namenames.frontend.views import Home, Friend

urlpatterns = patterns('namenames.frontend',

    # Examples:
    # url(r'^$', 'django_server.views.home', name='home'),

    #
    # This is the entry point for legacy
    #
    url(r'^friend$', Friend.as_view(), name='main_friends'),
    url(r'^$', Home.as_view(), name='main_home'),
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns