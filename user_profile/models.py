from django.db import models

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from exam.models import Exam

#################################
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.get_or_create(user=instance)


post_save.connect(create_user_profile, sender=User)

#################################

class RegisteredExam(models.Model):
    exam = models.ForeignKey(Exam)
    registeration_date = models.DateTimeField()
    is_done = models.BooleanField()

    user_profile = models.ForeignKey(UserProfile, related_name='registered_exams')




