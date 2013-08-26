from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import allauth
from allauth.account.views import LogoutView

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'namenames.frontend.home', name='home'),
    #url(r'^namenames/', include('namenames.frontend.urls')),

    #
    # All Auth
    #
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
    
    url(r'^accounts/allauth/logout/$', allauth.account.views.LogoutView.as_view(), name='logoutallauth'),
    (r'^accounts/', include('allauth.urls')),
    
    #
    #
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    #
    # this will catch all URLs and pass them into the frontend project. Use at the end
    #
    url(r'^', include('namenames.frontend.urls')),    
)
