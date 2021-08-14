from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
	path('', views.blog, name='home'),
	path('posts/', views.blog, name='posts'),
	path('post/<int:post_id>', views.blog_post, name='post'),
	path('contact/', views.contact, name='contact'),
	path('about/', views.about, name='about'),
	path('search/', views.search, name='search'),
	path('search_tag', views.search_tag, name='search-tag'),
	path('search_category', views.search_category, name='search-category'),

	# ---------------------------TESTING---------------------------
	path('create_post', views.create_post, name='create-post'),
	path('update_post/<int:post_id>', views.update_post, name='update-post'),
	path('delte_post/<int:post_id>', views.delete_post, name='delete-post'),
	path('add-post', views.add_post),
	path('reply', views.reply, name='reply'),

	path('login', views.login_user, name='login'),
	path('signup', views.signup, name='signup'),
	path('logout', views.logout_user, name='logout')
	
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
