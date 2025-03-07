from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm


## got it from here : https://docs.djangoproject.com/en/4.2/topics/auth/default/#auth-web-requests

def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.success(request, "There Was An Error Logging In, Try Again...")	
			return redirect('login')	


	else:
		return redirect('home')
#		return render(request, 'tools/home.html', {})
	
def logout_user(request):
	logout(request)
	messages.success(request, ("You Are Logged Out!"))
	return redirect('home')


def register_user(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			messages.success(request, ("Registration Successful! Please Log In to Continue ..."))
			return redirect('home')
	else:
		form = UserCreationForm()

	return render(request, 'auth/register_user.html', {
		'form':form,
		})
