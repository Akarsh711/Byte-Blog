from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from .models import *

from django.http import JsonResponse
from django.template.loader import render_to_string

from django.core.mail import send_mail
from django.contrib import messages

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth import authenticate, get_user_model, login, logout
# TODO
	# Find out an efficient way of Pagination as Current one is querying db in each page.
	# Create a function in admin.py which can add only tag if they aren't in table.
	# Relocate the form when adding Tags
	# Resolve time problem in js
	# add confirm password

	# CRITICAL
	# tag null problem
	# reduce redundancy
	# Dynamic Date time for reply
	# put ajax's code in try except for fail functionality to work

# DEV NOTES:
	# Search by Category is Disabled for now by enbaling null on category field in post model
	# JS datetime maybe buggy I don't know so keep an eye.
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
		# name = request.POST.get('name')
		# email = request.POST.get('email')
		print(request.POST.get('csrfmiddlewaretoken'))
		user = request.user
		subject = request.POST.get('subject')
		message = request.POST.get('message')
		post = Post.objects.filter(sno = post_id).first()
		obj=BlogComment(user = user, message = message, subject=subject, post=post, timestamp = datetime.datetime.strptime('2021-09-09 00:00:00','%Y-%m-%d %H:%M:%S'))
		obj.save()
		email = user.email
		send_mail(
			'Someone Commented'+subject,
		    'from:' +email +'\nmessage:\n'+message,
		    'rk7305758@gmail.com',
		    ['paliwalap7@gmail.com'],
		    fail_silently=True,
			)

		comments = BlogComment.objects.filter(post = post, parent = None)
		replies = BlogComment.objects.filter(post = post).exclude(parent = None)

		repliesdict  = {}
		for i in replies:
			if i.parent not in repliesdict.keys():
				repliesdict[i.parent] = [i]
			else:
				repliesdict[i.parent].append(i)
		print(repliesdict)
		context = {'comments':comments, 'repliesdict':repliesdict,'post':post}

		html = render_to_string('replycomment.html', context, request=request)
		return JsonResponse({'html':html})


	post = Post.objects.filter(sno = post_id).first()
	recent_posts = Post.objects.all()[:4:-1]
	tags = Tags.objects.filter(post=post)
	comments = BlogComment.objects.filter(post = post, parent=None)
	replies = BlogComment.objects.filter(post = post).exclude(parent = None)

	repliesdict  = {}
	for i in replies:
		if i.parent not in repliesdict.keys():
			repliesdict[i.parent] = [i]
		else:
			repliesdict[i.parent].append(i)

	print(repliesdict)
	return render(request, 'post-details.html', {'post':post, 'recent_posts':recent_posts, 'comments':comments, 'repliesdict':repliesdict, 'tags':tags})

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

# ------------------------ TESTING STUFF --------------------------------
def create_post(request):
	# usr = User.objects.create_user(username = 'jlo', password='bot')
	# usr.save()
	# t = Tags.objects.get(tag = 'First')
	# t.tag = 'oye'
	# t.save()
	# print(request.user, t)
	# post = Post.objects.filter(sno = 1).first()
	# recent_posts = Post.objects.all()[:4:-1]
	# comments = BlogComment.objects.filter(post = post)
	# tags = Tags.objects.filter(post=post)
	return render(request, 'add-post.html')
	return HttpResponse('running')


def add_post(request):
	import datetime
	import random
	if(request.method == 'POST'):

		title = request.POST.get('title')
		b_description = request.POST.get('bdescription')
		description = request.POST.get('description')
		author = request.user
		date = request.POST.get('date')
		dt = request.POST.get('datetime')

		thumbnail = request.FILES['thumbnail']

		print(',,,,,,,,,,,',thumbnail)
		tags = request.POST.get('tags')
		timestamp = datetime.datetime.strptime(dt,'%Y-%m-%d %H:%M:%S')
		# return  redirect('home')
		t = title.lower()
		slug = t.replace(' ', '-')
		slug = slug+str(random.randint(0, 9999))

		tag_objs = []
		print("in opst	")
		obj = Post(title = title, brief_description = b_description,content = description, author = author, slug=slug, timestamp=timestamp, thumbnail=thumbnail)
		obj.save()
		for tag in tags.split(','):
			print(tag)
			tag_obj, created = Tags.objects.get_or_create(
			    tag=tag,
			    defaults={'tag': tag},
			)
			# tag_objs.append(obj)
			obj.tags.add(tag_obj)
		obj.save()

	return render(request, 'add-post.html',)
	
def update_post(request, post_id):
	if request.method=='POST':
		post = Post.objects.filter(sno=post_id).filter(author = request.user).first()
		post.title = request.POST.get('title')
		post.brief_description = request.POST.get('bdescription')
		post.content = request.POST.get('description')
		image = request.FILES['thumbnail']
		dt = request.POST.get('datetime')
		post.timestamp = datetime.datetime.strptime(dt,'%Y-%m-%d %H:%M:%S')
		post.thumbnail = image
		post.save()

		return redirect('/')
	else:
		if request.user.is_authenticated:
			post = Post.objects.filter(sno=post_id).filter(author = request.user).first()
			if post is not None:
				print(post.tags.all())
				return render(request, 'update-post.html', {'post':post, 'tags':post.tags.all()})
		
		return HttpResponse('an error occured')
				# error

def delete_post(request, post_id):
	if request.user.is_authenticated:
		post = Post.objects.filter(sno=post_id).filter(author = request.user).first()
		if post is not None:
			post.delete()
		return redirect('/')

def reply(request):
	if request.method == "POST":
		print('request ai')

		user = request.user
		reply = request.POST.get('reply')
		post = Post.objects.filter(sno = int(request.POST.get('blogid'))).first()
		c_id = request.POST.get('c_id')
		comment_obj = BlogComment.objects.filter(sno=c_id).first()

		obj = BlogComment(user = user, post = post, message=reply, parent = comment_obj, timestamp = datetime.datetime.strptime('2021-09-09 00:00:00','%Y-%m-%d %H:%M:%S'))
		obj.save()
		
		comments = BlogComment.objects.filter(post = post, parent = None)
		replies = BlogComment.objects.filter(post = post).exclude(parent = None)

		repliesdict  = {}
		for i in replies:
			if i.parent not in repliesdict.keys():
				repliesdict[i.parent] = [i]
			else:
				repliesdict[i.parent].append(i)
		print(repliesdict)
		context = {'comments':comments, 'repliesdict':repliesdict,'post':post}
		blogid=request.POST.get('blogid')
		return redirect(f'/post/{blogid}')
		# html = render_to_string('replycomment.html', context, request=request)

		# return JsonResponse({'html':html})
	return HttpResponse('bad request')



def login_user(request):
	if request.method=='POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		user= authenticate(username =username, password = password)
	

		if user is None:
			User = get_user_model()
			user_queryset = User.objects.all().filter(email__iexact=username)

			if user_queryset:
			    username = user_queryset[0].username
			    user = authenticate(username=username, password=password)

		if user is not None:
		    login(request, user)
		    return redirect('/')
		else:

			return render(request, 'login.html', {'error':'Please fill correct Details'})
		    
		    
		# print("enter correct username and password or login with email")
		# 	return render(request,'login.html',{'a':"enter correct username and password or login with email"})
		


			# username

		'''login=SignUp.objects.filter(password=password).filter(username=username)
		if not login.exists():
			login=SignUp.objects.filter(email=username).filter(password=password)
	
			if not login.exists():
				print("user doesn't exists")
				return render(request,'login.html',{'a':"username and email doesn't exists"})
			else:
				print("loggedin with email")
		else:
			print("logged in with username")'''

		print (password)
	#print("try ,main aya")

	return render(request,'login.html',{'a':''})



def signup(request):
	
	if request.method=='POST':
		firstname = request.POST.get('firstname')
		lastname = request.POST.get('lastname')
		username=request.POST.get('username')
		email=request.POST.get('email')
		password=request.POST.get('password')
		print(",,,,,,,,,",firstname, lastname, username, email, password)
		obj=User.objects.create_user(username=username , email=email, password=password, first_name=firstname, last_name=lastname)
		obj.save()
		return redirect('/login')
	return render(request,'signup.html')
	

#def handlelogin(request):
	#return HttpResponse('login')

def logout_user(request):
	logout(request)
	#messages.success(request,"successfully logged out")
	return redirect('/')
