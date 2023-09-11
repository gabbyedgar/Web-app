from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('login', views.loginPage, name = "login"),
	path('home', views.home, name = "home"),
	path('about', views.about, name = "about"),
	path('subscribe', views.subscribe, name = "subcribe"),
	path('subscribed', views.subscribed, name = "subscribed"),
]