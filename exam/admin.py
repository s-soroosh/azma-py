from django.contrib import admin
from exam.models import *

admin.site.register(Exam)
admin.site.register(Question)
admin.site.register(Choice)
