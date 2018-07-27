from django.shortcuts import render
from .models import Post, Tag, Category

def posts(request):
	posts = Post.objects.all()
	categories = Category.objects.all()
	tags = Tag.objects.all()
	context = {
		'post_list': posts,
		'category_list': categories,
		'tag_list': tags,
	}

	return render(request, 'posts/posts.html', context)

def post(request, post_id):
	context = {
		'id': post_id,
	}
	return render(request, 'posts/post.html', context)

