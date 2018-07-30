from django.shortcuts import render
from .models import Post, Tag, Category
import math

count_per_page = 5

# fetch home posts list
def home(request):
	page = 1
	offset = count_per_page * (page - 1)
	limit = offset+count_per_page

	posts = Post.objects.all()[offset: limit]
	post_count = Post.objects.count()

	pagination_items = []

	if post_count <= count_per_page:
		pagination_item_count = 1
	else:
		pagination_item_count = math.ceil(post_count/count_per_page)

	for page in range(1, pagination_item_count+1):
		pagination_items.append(page)

	categories = Category.objects.all()
	tags = Tag.objects.all()

	context = {
		'post_list': posts,
		'category_list': categories,
		'tag_list': tags,
		'pagination_items': pagination_items,
		'type': None
	}

	return render(request, 'posts/posts.html', context)

# fetch all posts list
def posts(request, page):

	offset = count_per_page * (page - 1)
	limit = offset+count_per_page

	posts = Post.objects.all()[offset: limit]
	post_count = Post.objects.count()

	pagination_items = []

	if post_count <= count_per_page:
		pagination_item_count = 1
	else:
		pagination_item_count = math.ceil(post_count/count_per_page)

	for page in range(1, pagination_item_count+1):
		pagination_items.append(page)

	categories = Category.objects.all()
	tags = Tag.objects.all()

	context = {
		'post_list': posts,
		'category_list': categories,
		'tag_list': tags,
		'pagination_items': pagination_items,
		'type': None
	}

	return render(request, 'posts/posts.html', context)

# fetch post list for given taxonomy item
def taxonomy_posts(request, type, tax_id, page):
	offset = count_per_page * (page - 1)
	limit = offset+count_per_page

	if type == 'tag':
		pass
		current_tag = Tag.objects.get(pk=tax_id)
		sub_type = current_tag.name
		posts = Post.objects.filter(tag=current_tag)[offset: limit]
		post_count = Post.objects.filter(tag=current_tag).count()

	elif type == 'category':
		pass
		current_cat = Category.objects.get(pk=tax_id)
		sub_type = current_cat.name
		posts = Post.objects.filter(category=current_cat)[offset: limit]
		post_count = Post.objects.filter(category=current_cat).count()

	else:
		return


	if post_count <= count_per_page:
		pagination_item_count = 1
	else:
		pagination_item_count = math.ceil(post_count/count_per_page)

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
		'sub_type': sub_type,
		'sub_type_id': tax_id,
	}

	return render(request, 'posts/posts.html', context)

# fetch single post
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

