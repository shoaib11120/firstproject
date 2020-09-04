from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Post


def home(request):
	posts=Post.published.order_by('-publish')[:3]
	return render(request,
		'home/home.html',
		{'posts':posts,
		'nav':'home/files/nav.html',
		'cssF':'home/files/css.html',
		'jsF':'home/files/js.html',
		'myCarousel':'home/files/myCarousel.html'})
