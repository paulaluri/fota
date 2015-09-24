from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

# Used to create and manually log in a user
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

from fotalkapp.models import *
from fotalkapp.forms import *
from fotalkapp.helper import *

# Create your views here.
@login_required
def home(request):
	context = {}
	context['posts'] = Post.objects.all()
	
	try:
		context['latest'] = Post.objects.latest('id').id
	except:
		context['latest'] = 0

	context['cc'] = getCountryCode(request).lower()

	return render(request, "index.html", context)

@login_required
def post(request):
	context = {}

	if request.method != 'POST':
		return None

	form = PostForm(request.POST)
	context['form'] = form

	if not form.is_valid():
		return None

	post = form.save(commit=False)
	post.user = request.user
	post.save()
	form.save()

	context['status'] = "success"
	context['post'] = post

	return render(request, "post.html", context)

def register(request):
	context = {}

	#Render register page
	if request.method == 'GET':
		context['form'] = RegisterForm()
		return render(request, "register.html", context)

	#Register User
	form = RegisterForm(request.POST)
	context['form'] = form

	if not form.is_valid():
		return render(request, "register.html", context)

	user = form.save()
	user.set_password(request.POST['password'])
	user.is_active = True
	user.save()

	user = authenticate(username=request.POST['username'], \
                            password=request.POST['password'])
	login(request, user)

	return redirect(reverse('home'))