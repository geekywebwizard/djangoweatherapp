from os import name
from django.urls import path
from . import views

urlpatterns = [

 path( '', views.openweather, name='home'),
 path( 'home', views.home, name="home"),
 path('about', views.about, name='about'),
 path('contact', views.contact, name='contact'),
 path('open', views.openweather, name='open')

]