from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('orders/', views.orders, name='user_orders'),
    #path('(?P<id>\d+)/', views.remove_from_cart, name='remove_from_cart'),
    #path('(?P<slug>[\w-]+)/', views.add_to_cart, name='add_to_cart'),
]