from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def home(request):
    student = request.user.student
    classes = student.classes.first()
    lessons = classes.lesson_set.all()

    context = {'students':student,'classes':classes,'lessons':lessons}
    return render(request,'accounts/student.html',context)


def classes(request):
    student = request.user.student
    classes = student.classes.all()
    context = {'students': student, 'classes': classes,}
    return render(request, 'accounts/classes.html', context)


def lessons(request,id):
    lessons = Class.objects.get(id=id).lesson_set.all()
    # teacher = lessons[0].relate_class.teacher_set.first()

    context = {'lessons':lessons}
    return render(request,'accounts/lessons.html',context)


def update_profile(request):
    student = request.user.student
    form = StudentForm(instance=student)
    if request.method == 'POST' :
        form = StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            print('saved')
            return redirect('home')
    context = {'form': form}
    return render(request,'accounts/profile.html',context)


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None :
            login(request,user)
            print('user : ',user)
            return redirect('home')
    return render(request, 'accounts/login.html')
