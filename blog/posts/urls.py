from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
	path('posts/', views.posts),
	path('post/<int:post_id>/', views.post),
]