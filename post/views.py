from django.shortcuts import render, redirect
from django.http import HttpResponse

# https://www.figma.com/file/vFdiwBnNlrGvzAA0v5PxJl/%D0%A2%D0%B5%D1%81%D1%82%D0%BE%D0%B2%D0%BE%D0%B5-Kodland?node-id=0%3A1

from .forms import PostForm
from .models import Post

from django.core.paginator import Paginator

def posts_list(request):
	last = Post.objects.latest('date_pub')
	posts = Post.objects.order_by('-date_pub')[1:]

	# Первый параграф для последнего поста
	first_paragraph = last.body.split('\n')[0]

	# Использую пагинацию
	paginator = Paginator(posts, 9)

	page = paginator.get_page(1)
	return render(request, 'post/list.html',
			{
				'last': last,
				'posts': page.object_list,
				'first_paragraph': first_paragraph,
			}
		)

def post_create(request):
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('posts_list')
	else:
		form = PostForm()
	return render(request, 'post/create.html', {'form': form})

def post_detail(request, pk):
	post = Post.objects.get(pk=pk)
	return render(request, 'post/detail.html', {'post': post})