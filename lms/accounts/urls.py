from django.contrib import admin
from lms import settings
from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('classes/',views.classes,name='classes'),
    path('lessons/<int:id>/',views.lessons,name='lessons'),
    path('profile/',views.update_profile,name='profile'),
    path('login/',views.login_page,name='login'),
    path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('register',views.register_page,name='register'),
]