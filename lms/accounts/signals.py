from django.db.models.signals import post_save
from django.contrib.auth.models import User,Group
from django.dispatch import receiver
from .models import Student,Teacher


@receiver(post_save,sender=User)
def student_profile(sender,instance,created,**kwargs):
    if instance.student is None :
        if Group.objects.get(name='student') in instance.groups.all() :
            student = Student.objects.create(user=instance,fname=instance.username,email=instance.email)
            student.save()


# post_save.connect(student_profile,sender=User)
