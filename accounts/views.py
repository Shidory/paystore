from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import logout, login, authenticate

def logout_view(request):
    print("logging out")
    logout(request)
    return HttpResponseRedirect("/")

def login_view():
    form = LoginForm(request.POST or None)
