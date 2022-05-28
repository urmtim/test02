from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('info', views.info, name='about'),
    path('create', views.create, name='create'),
]