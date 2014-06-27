from django.contrib.auth.models import User
from django.db import models

class TutorialCategory(models.Model):
    name = models.CharField(max_length=120,primary_key=True)
    local_name = models.CharField(max_length=120,)
    parent = models.ForeignKey("self", null=True, blank=True, related_name='sub_categories')


class Tutorial(models.Model):
    category = models.ForeignKey(TutorialCategory)
    name = models.CharField(max_length=120,primary_key=True)
    local_name = models.CharField(max_length=150)
    author = models.ForeignKey(User)
    content = models.TextField()
    registered_date = models.DateTimeField()

