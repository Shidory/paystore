from django.shortcuts import render, Http404

from .models import Product, ProductImage

def home(request):
    products = Product.objects.all()
    template = 'products/home.html'
    context = {"products": products}
    return render(request, template, context)


def all(request):
    products = Product.objects.all()
    context = {"products": products}
    template = 'products/all.html'
    return render(request, template, context)

def single(request, slug):
    try:
        product = Product.objects.get(slug=slug)
        context = {"product": product}
        template = 'products/single.html'
        return render(request, template, context)
    except:
        raise Http404

def search(request):
    try:
        q = request.Get.get('q')
    except:
        q = None
    if q:
        context = {"query": q}
        template = 'products/results.html'
    else:
        template = 'products/home.html'
        context = {}
    return render(request, template, context)