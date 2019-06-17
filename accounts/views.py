from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return render(request, 'home.html')
            else:
                messages.error(request, 'Username and password did not matched!')
        except auth.ObjectNotExist():
            print("Invalid user")

    return render(request, 'login.html')


def logout_view(request):
    print("logging out")
    logout(request)
    return HttpResponseRedirect("/")

