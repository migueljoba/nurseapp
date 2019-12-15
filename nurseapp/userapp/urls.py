from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='index'),
    path('login/', views.login, name='login-controller'),
    path('logout/', views.logout, name='logout-controller'),
    path('home', views.home, name='home-controller'),
]
