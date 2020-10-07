from django.urls import path

from .views import request_oauth_token, request_access_token

app_name = 'twitter_toplinks'

urlpatterns = [
	path('request_token', request_oauth_token, name='request_token'),
	path('access_token', request_access_token, name='access_token')
]