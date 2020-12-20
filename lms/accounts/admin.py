from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Department)
admin.site.register(Major)
admin.site.register(Class)
admin.site.register(Lesson)
admin.site.register(Homework)
admin.site.register(Exam)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(HomeworkAnswer)