from django.contrib import admin
from django import forms
from feincms.contrib.richtext import RichTextFormField
from tutorial.models import TutorialCategory, Tutorial

admin.site.register(TutorialCategory)
admin.site.register(Tutorial)
