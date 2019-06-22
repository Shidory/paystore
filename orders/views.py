import time
from django.shortcuts import render, HttpResponseRedirect

from carts.models import Cart
from .models import Order
from django.urls import reverse

def orders(request):
    context = {}
    template = "user.html"
    return render(request, template, context)

def checkout(request):
    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except:
        the_id = None
        return HttpResponseRedirect(reverse("cart"))
    new_order, created = Order.objects.get_or_create(cart=cart)
    if created:
        new_order.order_id = str(time.time())
        new_order.save()
    if new_order.status == "Finished":
        cart.delete()
        del request.session['cart_id']
        del request.session['items_total']
        return HttpResponseRedirect(reverse("cart"))

    context = {}
    template = "home.html"
    return render(request, template, context)
