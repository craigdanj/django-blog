from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
	path('posts/<int:page>/', views.posts, name='posts'),
	path('post/<int:post_id>/', views.post, name='post'),
]