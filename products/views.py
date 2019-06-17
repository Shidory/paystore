from django.shortcuts import render

from .models import Product

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

def single(request, id):
    try:
        product = Product.objects.get(id=id)
        print(product.title)
        products = Product.objects.all()
        context = {"products": products}
        template = 'products/all.html'
        return render(request, template, context)
    except:
        pass