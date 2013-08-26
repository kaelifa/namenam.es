from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#
# Import class based views
#
import namenames.frontend.views
from namenames.frontend.views import Home

urlpatterns = patterns('namenames.frontend',

    # Examples:
    # url(r'^$', 'django_server.views.home', name='home'),

    #
    # This is the entry point for legacy
    #
    #url(r'^home$', 'views.Home.as_view()'),
    url(r'^$', Home.as_view()),
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns