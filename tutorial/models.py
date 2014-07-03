from django.contrib.auth.models import User
from django.db import models
from jdatetime import datetime as jalali_datetime
from tinymce.models import HTMLField


class TutorialCategory(models.Model):
    class Meta:
        ordering = ['order']
    name = models.CharField(max_length=120, primary_key=True)
    local_name = models.CharField(max_length=120, )
    parent = models.ForeignKey("self", null=True, blank=True, related_name='sub_categories')
    description = HTMLField(default="Without description")
    img_address = models.CharField(default='image/techs/python.png', max_length=200)
    order = models.IntegerField(default=1)

    def __unicode__(self):
        return self.local_name


class Tutorial(models.Model):
    class Meta:
        ordering = ['-registered_date']

    category = models.ForeignKey(TutorialCategory, related_name='tutorials')
    keyword = models.CharField(max_length=200)  # comma separated
    abstract = HTMLField()
    name = models.CharField(max_length=120, primary_key=True)
    local_name = models.CharField(max_length=150)
    author = models.ForeignKey(User)
    content = HTMLField()
    registered_date = models.DateTimeField()

    def get_persian_registered_date(self):
        return jalali_datetime.fromgregorian(datetime=self.registered_date).strftime('%Y/%m/%d')

    def __unicode__(self):
        return self.local_name


