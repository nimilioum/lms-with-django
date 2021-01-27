from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def home(request):
    student = request.user.student
    classes = student.get_classes()
    # lessons = classes.lesson_set.all()

    # context = {'students':student,'classes':classes,'lessons':lessons}
    context = {'student': student, 'classes': classes}
    return render(request,'accounts/student.html',context)


@login_required
def classes(request):
    student = request.user.student
    classes = student.get_classes()
    context = {'students': student, 'classes': classes,}
    return render(request, 'accounts/classes.html', context)


@login_required
def lessons(request,id):
    # lessons = request.user.student.get_lessons()     # this will be used in Home page
    lessons = Class.objects.get(id=id).get_lessons()

    context = {'lessons':lessons}
    return render(request,'accounts/lessons.html',context)


@login_required
def update_student(request):
    student = request.user.student
    form = StudentForm(instance=student)
    if request.method == 'POST' :
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request,'accounts/profile.html',context)


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None :
            # print('***   ',user.id)
            login(request,user)
            # print('user : ',user)
            return redirect('home')
    return render(request, 'accounts/login.html')


def register_page(request):
    form = CreateUser()

    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form' : form}
    return render(request,'accounts/register.html',context)
