from relation.forms import NewUserForm
from django.shortcuts import render


# login-logout
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
	return render(request,'index.html')


def home(request):
	return render(request,'home.html')


def profile(request):
	return render(request,'profile.html')

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))


def signup(request):
	registered = False

	if request.method == "POST":
		user_form = NewUserForm(data=request.POST)

		if user_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			registered = True
		else:
			print(user_form.errors)
	else:
		user_form = NewUserForm()
	return render(request,'signup.html',
						{'user_form':user_form,})


def user_login(request):
	if request.method == 'POST':
		# contactNumber = request.POST.get('contactnumber')
		password = request.POST.get('password')

		user = authenticate(password=password)

		if user:
			if user.is_active:
				login(request,user)
				return HttpResponseRedirect(reverse('home'))

			else:
				return HttpResponse("account not active.")
		else:
			print("Someone tried to login and failed!")
			# print("Username:{} and password:{}".format(username,password))
			return HttpResponse("invalid login details supplied!")
	else:
		return render(request,'login.html',{})
