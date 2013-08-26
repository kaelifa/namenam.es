from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'namenames.frontend.home', name='home'),
    #url(r'^namenames/', include('namenames.frontend.urls')),

    #
    #
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    #
    # this will catch all URLs and pass them into the frontend project. Use at the end
    #
    url(r'^', include('namenames.frontend.urls')),    
)
