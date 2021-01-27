from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django import forms
from django.contrib.auth.models import User
from .models import *


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['fname', 'lname', 'email','image']
        widgets = {
            'image' : forms.FileInput(attrs={'class':'form-control-file'})
        }


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
        widgets = {
            'fname': forms.TextInput(attrs={'type': 'text'}),
        }


# class UserForm()


class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username' : forms.TextInput(attrs={'type':'text','placeholder':'e.g : Jack123'}),
            'email': forms.TextInput(attrs={'type': 'text', 'placeholder': 'e.g : example@fakemail.com'}),
            'password1' : forms.TextInput(attrs={'type':'password'}),
            'password2': forms.TextInput(attrs={'type': 'password'})
        }