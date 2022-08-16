from xml.dom.minidom import Document
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from home import views 

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
    path('card_list', views.card_list, name='card_list'),
    path('signup', views.signup and views.handleSignUp, name='signup'),
    path('login', views.handleLogin, name='handleLogin'),
    path('logout', views.handleLogout, name='handleLogout'),
    path('client', views.client, name='client'),
    path('auth', views.auth, name='auth'),
    path('mail', views.mail, name='mail'),
]
