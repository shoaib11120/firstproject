from django.urls import path
from .views import apiPostDetail,apiPostList,apiPostDetailUpdate,apiPostDetailDelete,apiPostDetailCreate

app_name = 'blog'

urlpatterns = [
	path('create',
		apiPostDetailCreate,
		name="post_create"),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
		apiPostDetail,
		name='post_detail'),
	path('<int:year>/<int:month>/<int:day>/<slug:post>/update',
		apiPostDetailUpdate,
		name='post_detail_update'),
	path('<int:year>/<int:month>/<int:day>/<slug:post>/delete',
		apiPostDetailDelete,
		name='post_detail_delete'),
	path('',
		apiPostList,
		name='post_list'),
]