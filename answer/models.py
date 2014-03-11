from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from exam.models import Question, Exam, Choice


class ExamAnswer(models.Model):
    user = models.ForeignKey(User)
    exam = models.ForeignKey(Exam)


class Answer(models.Model):
    question = models.ForeignKey(Question)
    exam_answer = models.ForeignKey(ExamAnswer, related_name='answers')
    selected_choices = models.ManyToManyField(Choice, related_name='cho+')
