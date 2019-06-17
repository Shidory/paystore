from django.urls import path
from . import views

urlpatterns = [
    path('all', views.all, name='all'),
    path('', views.home, name='home'),
    path('(?P<id>\+d)/', views.single, name='single_product'),
]
