from django.contrib import admin
from django import forms
from feincms.contrib.richtext import RichTextFormField
from tutorial.models import TutorialCategory, Tutorial, TutorialExam

admin.site.register(TutorialCategory)
admin.site.register(Tutorial)
admin.site.register(TutorialExam)
