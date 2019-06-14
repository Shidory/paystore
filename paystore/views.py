from django.shortcuts import render

def home(request):
    template = 'base.html'
    context = locals()
    return render(request, template, context)