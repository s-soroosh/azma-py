# -*- coding: utf8 -*-
from django.contrib import admin
from django import forms

from exam.models import *


class ChoiceForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea)


class QuestionForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea)
    code = forms.CharField(widget=forms.Textarea,required=False)


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0
    form = ChoiceForm


class QuestionAdmin(admin.ModelAdmin):
    model = Question
    inlines = [ChoiceInline]


class QuestionInline(admin.TabularInline):
    model = Question
    readonly_fields = ['exam']
    extra = 4


class ExamAdmin(admin.ModelAdmin):
    # date_hierarchy = 'start_date'
    fieldsets = [
        ('عمومی', {'fields': ('name', 'local_name','exam_state')}),
        (None, {'fields': ('start_date', 'description', 'duration', 'category')})
    ]
    inlines = [QuestionInline]


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    form = QuestionForm


admin.site.register(Exam, ExamAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(ExamCategory)
# admin.site.register(Choice)
