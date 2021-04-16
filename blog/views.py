from django.shortcuts import render
from .models import *

from django.http import JsonResponse
from django.template.loader import render_to_string

from django.core.mail import send_mail
from django.contrib import messages

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# TODO
	# Find out an efficient way of Pagination as Current one is querying db in each page.
	# Comment's Submit Button Gif ...Done
	# Feautred Posts ...Done
	# Category and Tag Search ...Done
	
def featured_posts(request):
	featured_posts = FeaturedPost.objects.all()
	return {
	    'featured_posts': featured_posts
	}

def home(request):
	# Pagination logic using Django's Paginator
	
	posts = Post.objects.all()[:4]
	return render(request, 'index.html', {'posts':posts, 'post_list':posts[::-1]})

def blog(request):
	featured_posts = FeaturedPost.objects.all()
	posts = Post.objects.all()
	page = request.GET.get('page', 1)
	paginator = Paginator(posts, 2)
	categories = Category.objects.all()
	try:
	    numbers = paginator.page(page)
	except PageNotAnInteger:
	    numbers = paginator.page(1)
	except EmptyPage:
	    numbers = paginator.page(paginator.num_pages)

	return render(request, 'blog.html', {'numbers':numbers, 'featured_posts':featured_posts, 'categories':categories})

def blog_post(request, post_id):
	if(request.method == 'POST'):
		name = request.POST.get('name')
		email = request.POST.get('email')
		subject = request.POST.get('subject')
		message = request.POST.get('message')
		post = Post.objects.filter(sno = post_id).first()
		obj=BlogComment(name=name, message =message, email=email, subject=subject, post=post)
		obj.save()

		send_mail(
			'Someone Commented'+subject,
		    'from:' +email +'\nmessage:\n'+message,
		    'rk7305758@gmail.com',
		    ['paliwalap7@gmail.com'],
		    fail_silently=True,
			)

		comments = BlogComment.objects.filter(post = post)
		context = {'comments':comments, 'post':post}

		html = render_to_string('comments.html', context, request=request)
		return JsonResponse({'html':html})


	post = Post.objects.filter(sno = post_id).first()
	recent_posts = Post.objects.all()[:4:-1]
	comments = BlogComment.objects.filter(post = post)
	tags = Tags.objects.filter(post=post)


	return render(request, 'post-details.html', {'post':post, 'recent_posts':recent_posts, 'comments':comments, 'tags':tags})

def contact(request):
	if request.method=='POST':
		name = request.POST.get('name')
		email = request.POST.get('name')
		subject = request.POST.get('name')
		message = request.POST.get('name')

		try:	
			send_mail(
				subject,
			    'from:' +email +'\nmessage:\n'+message,
			    'rk7305758@gmail.com',
			    ['paliwalap7@gmail.com'],
			    fail_silently=False,
				)
			messages.success(request, 'Mail Sent Successfully')
		except:
			messages.error(request, 'Mail Sent Failed! Some Error Occured')

	return render(request, 'contact.html')

def about(request):
	return render(request, 'about.html')

def search(request):

	query = request.GET.get('q')
	posts = Post.objects.filter(title__contains = query)
	page = request.GET.get('page', 1)
	paginator = Paginator(posts, 2)
	categories = Category.objects.all()
	try:
	    post_obj = paginator.page(page)
	except PageNotAnInteger:
	    post_obj = paginator.page(1)
	except EmptyPage:
	    post_obj = paginator.page(paginator.num_pages)
	
	return render(request, 'search.html', {'post_obj':post_obj, 'categories':categories, 'results_count':posts.count(), 'query':query})


def search_tag(request):
	query = request.GET.get('tag')
	posts = Post.objects.filter(tags__tag__contains = query)
	page = request.GET.get('page', 1)
	paginator = Paginator(posts, 2)
	categories = Category.objects.all()
	try:
	    post_obj = paginator.page(page)
	except PageNotAnInteger:
	    post_obj = paginator.page(1)
	except EmptyPage:
	    post_obj = paginator.page(paginator.num_pages)
	
	return render(request, 'search.html', {'post_obj':post_obj, 'categories':categories, 'results_count':posts.count(), 'query':query})

def search_category(request):
	query = request.GET.get('category')
	posts = Post.objects.filter(category__name= query)
	page = request.GET.get('page', 1)
	paginator = Paginator(posts, 2)
	categories = Category.objects.all()
	try:
	    post_obj = paginator.page(page)
	except PageNotAnInteger:
	    post_obj = paginator.page(1)
	except EmptyPage:
	    post_obj = paginator.page(paginator.num_pages)
	
	return render(request, 'search.html', {'post_obj':post_obj, 'categories':categories, 'results_count':posts.count(), 'query':query})

