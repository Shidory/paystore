from django.shortcuts import render

def home(request):
    if request.user.is_authenticated():
        username = "Shidory"
        context = {"username": request.user}
    else:
        context = {"username": request.user}
        
    template = 'products/home.html'
    context = locals()
    return render(request, template, context)