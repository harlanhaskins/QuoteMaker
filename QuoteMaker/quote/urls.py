from django.conf.urls import patterns, include, url
from django.contrib.auth import views as auth_views
from . import views
from . import api

# Make sure to end each URL pattern with '/?$' to make sure the end of the url
# properly handles omitting the trailing slash.
urlpatterns = patterns('',
    url(r'login/?$', views.login_view, name='login'),
    url(r'logout/?$', views.logout_view, name='logout'),
    url(r'signup/?$', views.signup, name='signup'),
    url(r'search/?$', views.search, name='search'),
    url(r'create/?$', views.create, name='create'),
    url(r'api/quotes/(?P<path>.+)/?$', api.quote, name='api_quote'),
    url(r'delete/(?P<path>.+)/?$', views.delete, name='delete'),
    url(r'(?P<path>.+)/?$', views.quote, name='quote'),
    url(r'^/?$', views.home, name='home'),
)
