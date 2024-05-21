from django.urls import path, include
from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.signin, name='signin'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('homepage/', views.homepage, name='homepage'),
    path('drinks/', views.drinks, name='drinks'),
    path('food/', views.food, name='food'),
    path('goodbye/', views.goodbye, name='goodbye'),    
]





