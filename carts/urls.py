from django.urls import path
from . import views

urlpatterns = [
    path('', views.view, name='cart'),
    path('(?P<slug>[\w-]+)/', views.add_to_cart, name='add_to_cart'),
]
