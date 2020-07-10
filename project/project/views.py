from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Post


def home(request):
	posts=Post.published.order_by('-publish')[:3]
	return render(request,
		'home.html',
		{'posts':posts,'nav':'nav.html'})

def category(request):
	return render(request,'category.html',{'nav':'nav.html'})

def post_latest(request):
	posts=Post.published.order_by('-pub_date')[:3]
	return render(request,
		'home.html',
		{'posts':posts})