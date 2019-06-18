from django.urls import path
from . import views

urlpatterns = [
    path('all', views.all, name='all'),
    path('all/(?P<slug>[\w-]+)/', views.single, name='single_product'),
    path('', views.home, name='home'),
    path('s/', views.search, name='search'),
]
