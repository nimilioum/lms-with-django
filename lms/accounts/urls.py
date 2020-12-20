from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('classes/',views.classes,name='classes'),
    path('lessons/<int:id>/',views.lessons,name='lessons'),
    path('profile/',views.update_profile,name='profile'),
    path('login/',views.login_page,name='login')
]