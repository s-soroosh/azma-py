from django.contrib.auth.models import User
from django.db import models
from jdatetime import datetime as jalali_datetime


class TutorialCategory(models.Model):
    name = models.CharField(max_length=120, primary_key=True)
    local_name = models.CharField(max_length=120, )
    parent = models.ForeignKey("self", null=True, blank=True, related_name='sub_categories')
    description = models.TextField(default="Without description")


class Tutorial(models.Model):
    category = models.ForeignKey(TutorialCategory, related_name='tutorials')
    keyword = models.CharField(max_length=200)  # comma separated
    name = models.CharField(max_length=120, primary_key=True)
    local_name = models.CharField(max_length=150)
    author = models.ForeignKey(User)
    content = models.TextField()
    registered_date = models.DateTimeField()

    def get_persian_registered_date(self):
        return jalali_datetime.fromgregorian(datetime=self.registered_date).strftime('%Y/%m/%d')


