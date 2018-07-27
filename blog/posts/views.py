from django.shortcuts import render
from .models import Post, Tag, Category

def posts(request, page):
	count_per_page = 5
	offset = count_per_page * page
	limit = offset+count_per_page

	posts = Post.objects.all()[offset: limit]
	post_count = Post.objects.count()
	categories = Category.objects.all()
	tags = Tag.objects.all()
	
	pagination_items = []
	pagination_item_count = post_count%count_per_page

	for page in range(1, pagination_item_count+1):
		pagination_items.append(page)

	context = {
		'post_list': posts,
		'category_list': categories,
		'tag_list': tags,
		'pagination_items': pagination_items
	}

	return render(request, 'posts/posts.html', context)

def post(request, post_id):

	post = Post.objects.get(pk=post_id)
	categories = Category.objects.all()
	tags = Tag.objects.all()

	context = {
		'id': post_id,
		'post': post,
		'category_list': categories,
		'tag_list': tags,
	}

	return render(request, 'posts/post.html', context)

