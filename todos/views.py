from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Users, UserData


def index(request):
	template = loader.get_template('index.html')
	return HttpResponse(template.render())

def signup(request):
	template = loader.get_template('signup.html')
	return HttpResponse(template.render({'user': False}, request))

def login(request):
	template = loader.get_template('login.html')
	return HttpResponse(template.render({'user': False}, request))

def adduser(request):
	name = request.POST['name']
	email = request.POST['email']
	password = request.POST['password']
	confirm_password = request.POST['confirm_password']

	template = loader.get_template('signup.html')

	if name == '':
		context = {
			'error': 'name field is empty' 
		}
		return HttpResponse(template.render(context, request))

	if email == '':
		context = {
			'error': 'email field is empty' 
		}
		return HttpResponse(template.render(context, request))

	if password == '':
		context = {
			'error': 'password field is empty' 
		}
		return HttpResponse(template.render(context, request))

	if password == confirm_password:
		user = Users(name=name, email=email, password=password)
		user.save()
		return HttpResponseRedirect(reverse('login'))
	else:
		context = {'error': 'password did not match',}
		return HttpResponse(template.render(context, request))

def loguser(request):
	email = request.POST['email']
	password = request.POST['password']

	user = Users.objects.filter(email=email, password=password).first()

	if user:
		request.session['userid'] = user.id
		return redirect(reverse('user'))
	return HttpResponseRedirect(reverse('login'))

def user(request):
	template = loader.get_template('user.html')
	id = request.session.get('userid', None)
	context = {
		'userdata': UserData.objects.filter(user_id=id)
	}
	return HttpResponse(template.render(context, request))

def add(request):
	template = loader.get_template('addtodo.html')
	return HttpResponse(template.render({}, request))

def addtodo(request):
	id = request.session.get('userid', None)
	title = request.POST['title']
	description = request.POST['description']
	data = UserData(user_id=id, title=title, description=description)
	data.save()
	return HttpResponseRedirect(reverse('user'))

def deletedata(request, id):
	data = UserData.objects.get(id=id)
	data.delete()
	return HttpResponseRedirect(reverse('user'))

def logout(request):
	del request.session['userid']
	return HttpResponseRedirect(reverse('index'))

def update(request, id):
	template = loader.get_template('updatetodo.html')
	data = UserData.objects.get(id=id)
	context = {
		'data': data,
	}
	return HttpResponse(template.render(context, request))

def updatetodo(request, id):
	data = UserData.objects.get(id=id)
	data.title = request.POST['title']
	data.description = request.POST['description']
	data.save()
	return HttpResponseRedirect(reverse('user'))

def test(request):
	template = loader.get_template('test.html')
	context = {
		'users': Users.objects.all(),
	}
	return HttpResponse(template.render(context, request))
