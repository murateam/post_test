from django.urls import path

from .views import *

urlpatterns = [
	path('', posts_list, name='posts_list'),
	path('create', post_create, name='post_create'),
	path('<int:pk>', post_detail, name='post_detail'),
]