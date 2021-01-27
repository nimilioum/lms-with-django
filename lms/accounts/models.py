from django.db import models
from django.contrib.auth.models import User,AbstractUser
from datetime import datetime
import random


def get_path(instance,filename):
    id = instance.student_id
    now = datetime.now()
    time = now.strftime('%d_%H')
    date = now.strftime('%Y_%m')
    end = filename.split('.')[-1]
    return date + '/' + time +'_'+ id + '.' + end


# Create your models here.
# class LMSUser(AbstractUser):
#     is_student = models.BooleanField()
#     is_teacher = models.BooleanField()
#     is_lms_staff = models.BooleanField()
#
#     def __str__(self):
#         return self.username


class Department(models.Model):
    name = models.CharField(max_length=100, null=True, default=' ')

    def __str__(self):
        return self.name


class Major(models.Model):
    name = models.CharField(max_length=100, null=True, default=' ')
    department = models.ForeignKey(Department, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Class(models.Model):
    name = models.CharField(max_length=100, null=True, default=' ')
    major = models.ForeignKey(Major, null=True, on_delete=models.CASCADE)

    def get_lessons(self):
        return self.lesson_set.all()

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(max_length=100, null=True, default=' ')
    date = models.DateTimeField(null=True)
    relate_class = models.ForeignKey(Class, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Homework(models.Model):
    name = models.CharField(max_length=100, null=True, default=' ')
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    relate_class = models.ForeignKey(Class, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Exam(models.Model):
    name = models.CharField(max_length=100, null=True, default=' ')
    date = models.DateTimeField(null=True)
    relate_class = models.ForeignKey(Class, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Student(models.Model):
    fname = models.CharField(max_length=100, null=True, default=' ')
    lname = models.CharField(max_length=100, null=True, default=' ')
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    email = models.EmailField(null=True)
    image = models.ImageField(null=True,upload_to=get_path,default='profile.png')
    student_id = models.CharField(max_length=15, null=True, default=' ')
    department = models.ForeignKey(Department, null=True, on_delete=models.SET_NULL)
    classes = models.ManyToManyField(Class)

    def get_classes(self):
        class_list = self.classes.all()
        return class_list

    def get_lessons(self):
        class_list = self.get_classes()
        lessons = class_list.none()
        for cls in class_list:
            lessons = lessons | cls.get_lessons()
        return lessons

    def __str__(self):
        return str(self.fname) + ' ' + str(self.lname)


class Teacher(models.Model):
    fname = models.CharField(max_length=100, null=True, default=' ')
    lname = models.CharField(max_length=100, null=True, default=' ')
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    teacher_id = models.CharField(max_length=15, null=True, default=' ')
    department = models.ForeignKey(Department, null=True, on_delete=models.SET_NULL)
    classes = models.ManyToManyField(Class)

    def __str__(self):
        return str(self.fname) + ' ' + str(self.lname)


class Staff(models.Model):
    fname = models.CharField(max_length=100, null=True, default=' ')
    lname = models.CharField(max_length=100, null=True, default=' ')
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    teacher_id = models.CharField(max_length=15, null=True, default=' ')
    department = models.ForeignKey(Department, null=True, on_delete=models.SET_NULL)
    classes = models.ManyToManyField(Class)

    def get_classes(self):
        class_list = self.classes.all()
        return class_list

    # def get_lessons(self):
    #     lessons = None
        # class_list = self.get_

    def __str__(self):
        return str(self.fname) + ' ' + str(self.lname)


class HomeworkAnswer(models.Model):
    description = models.CharField(max_length=1000, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    file = models.FileField()
    student = models.ForeignKey(Student, null=True, on_delete=models.CASCADE)
