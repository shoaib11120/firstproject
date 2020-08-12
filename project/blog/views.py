from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator,EmptyPage,\
	PageNotAnInteger
from .models import Post
from .forms import EmailPostForm
from django.core.mail import send_mail


# region Post List

def post_list(request):
	posts=Post.published.all()
	paginator = Paginator(posts,8)
	page=request.GET.get('page')
	try:
		newPosts=paginator.page(page)
	except PageNotAnInteger:
		newPosts=paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	return render(request,
		'blog/post/list.html',
		{'page':page,
		'posts':newPosts,
		'nav':'blog/post/files/nav.html',
		'js':'blog/post/files/js.html',
		'css':'blog/post/files/css.html',
		'postList':'blog/post/files/postList.html',
		'postListPaginator':'blog/post/files/postListPaginator.html'})

# endregion

# region post detail

def post_detail(request,year,month,day,post):
	post=get_object_or_404(Post,
		slug=post,
		status='published',
		publish__year=year,
		publish__month=month,
		publish__day=day,)
	return render(request,
		'blog/post/detail.html',
		{'post':post,
		'nav':'blog/post/files/nav.html',
		'css':'blog/post/files/blogDetailCss.html'})

# endregion

# region Post Share

def postShare(request,post_id):
	post=get_object_or_404(Post,id=post_id,status='published')
	sent= False
	if request.method=='POST':
		form=EmailPostForm(request.POST)
		if form.is_valid():
			cd=form.cleaned_data
			post_url = request.build_absolute_uri(post.get_absolute_url())
			subject = '{}({})recommneds you reading "{}"'.format(cd['name'],cd['email'],post.title)
			message = 'Read "{}" at {} \n \n {}\'s comments:{}'.format(post.title,post_url,cd['name'],cd['comments'])
			send_mail(subject,message,"admin@myblog.com",[cd['to']])
			sent = True
	else:
		form=EmailPostForm()
	return render(request,
			'blog/post/files/share.html',
			{'post':post,
			 'form':form,
			 'sent':sent,
			 'css':'blog/post/files/postShareCss.html'})


# endregion
