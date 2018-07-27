from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
	path('posts/<int:page>/', views.posts, name='posts'),
	path('<str:type>/<int:tax_id>/<int:page>/', views.taxonomy_posts, name='posts'),
	path('post/<int:post_id>/', views.post, name='post'),
]