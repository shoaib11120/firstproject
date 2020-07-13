from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from uuid import uuid4
import os


#Manager of published posts
class PublishedManager(models.Manager):
	def get_queryset(self):
		return super(PublishedManager,
			self).get_queryset()\
		.filter(status='published')

#change image name
def path_and_rename(instance,filename):
	upload_to='blogThumbnails'
	ext=filename.split('.')[-1]
	if instance.pk:
		filename='{}.{}'.format(instance.pk,
			ext)
	else:
		filename='{}.{}'.format(uuid4().hex,
			ext)
	return os.path.join(upload_to,filename)


# Create your models here.
class Post(models.Model):
	STATUS_CHOICES=(
		('draft','Draft'),
		('published','Published'),
		)
	title=models.CharField(max_length=250)
	slug=models.SlugField(max_length=250,
		unique_for_date='publish'
		)
	author = models.ForeignKey(User,
		on_delete=models.CASCADE,
		related_name='blog_posts')
	thumbnail=models.ImageField(upload_to=path_and_rename,
		default='default.jepg')
	body=models.TextField()
	publish=models.DateTimeField(default=timezone.now)
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)
	status=models.CharField(max_length=10,
		choices=STATUS_CHOICES,
		default='draft')
	objects=models.Manager()
	published=PublishedManager()

	class Meta:
		ordering=('-publish',)

		def __str__(self):
			return self.title

	def get_absolute_url(self):
		return reverse('blog:post_detail',
			args=[self.publish.year,
			self.publish.month,
			self.publish.day,
			self.slug])


