from django.forms import ModelForm
from django import forms
from .models import *


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['fname','lname','email']


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
        widgets = {
            'fname': forms.TextInput(attrs={'type':'text',}),
        }