from django.shortcuts import render
from .models import Post, Tag, Category

def posts(request, page):
	count_per_page = 5
	offset = count_per_page * (page - 1)
	limit = offset+count_per_page

	posts = Post.objects.all()[offset: limit]
	post_count = Post.objects.count()

	pagination_items = []
	pagination_item_count = post_count%count_per_page

	for page in range(1, pagination_item_count+1):
		pagination_items.append(page)

	categories = Category.objects.all()
	tags = Tag.objects.all()

	context = {
		'post_list': posts,
		'category_list': categories,
		'tag_list': tags,
		'pagination_items': pagination_items
	}

	return render(request, 'posts/posts.html', context)


def taxonomy_posts(request, type, tax_id, page):
	count_per_page = 5
	offset = count_per_page * (page - 1)
	limit = offset+count_per_page

	if type == 'tag':
		pass
		current_tag = Tag.objects.get(pk=tax_id)
		sub_type = current_tag.name
		posts = Post.objects.filter(tag=current_tag)[offset: limit]

	elif type == 'category':
		pass
		current_cat = Category.objects.get(pk=tax_id)
		sub_type = current_cat.name
		posts = Post.objects.filter(category=current_cat)[offset: limit]
	else:
		return

	post_count = len(posts)
	
	if post_count < count_per_page:
		pagination_item_count = 1
	else:
		pagination_item_count = post_count%count_per_page

	pagination_items = []

	for page in range(1, pagination_item_count+1):
		pagination_items.append(page)


	categories = Category.objects.all()
	tags = Tag.objects.all()

	context = {
		'post_list': posts,
		'category_list': categories,
		'tag_list': tags,
		'pagination_items': pagination_items,
		'type': type,
		'sub_type': sub_type
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

