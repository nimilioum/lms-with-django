from django.db import models
from django.contrib.auth.models import User


# Create your models here.
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
    student_number = models.CharField(max_length=15, null=True, default=' ')
    department = models.ForeignKey(Department, null=True, on_delete=models.SET_NULL)
    classes = models.ManyToManyField(Class)

    def __str__(self):
        return str(self.fname) + ' ' + str(self.lname)


class Teacher(models.Model):
    fname = models.CharField(max_length=100, null=True, default=' ')
    lname = models.CharField(max_length=100, null=True, default=' ')
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    student_number = models.CharField(max_length=15, null=True, default=' ')
    department = models.ForeignKey(Department, null=True, on_delete=models.SET_NULL)
    classes = models.ManyToManyField(Class)

    def __str__(self):
        return str(self.fname) + ' ' + str(self.lname)


class HomeworkAnswer(models.Model):
    description = models.CharField(max_length=1000, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    file = models.FileField()
    student = models.ForeignKey(Student, null=True, on_delete=models.CASCADE)
