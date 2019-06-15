from django.shortcuts import render


def home(request):
    if request.user.is_authenticated():
        username = "Shidory"
        context = {"username": request.user}
    else:
        context = {"username": request.user}
    template = 'products/home.html'
    return render(request, template, context)


def all(request):
    context = {"products": Product.objects.all()}
    template = 'products/all.html'
    return render(request, template, context)