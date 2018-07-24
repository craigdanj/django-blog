from django.shortcuts import render

# Create your views here.

def posts(request):
	context = {}
	return render(request, 'posts/posts.html', context)

def post(request, post_id):
	context = {
		'id': post_id,
	}
	return render(request, 'posts/post.html', context)