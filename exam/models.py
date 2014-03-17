import os
import datetime
from django.db import models
from django.db.models import Sum, Count
from django.utils.encoding import force_text, force_str


class ExamCategory(models.Model):
    name = models.CharField(max_length=200)
    local_name = models.CharField(max_length=200)
    parent = models.ForeignKey("self", null=True, related_name='sub_categories')


    def number_of_exams(self):
        return self.exam_set.count()

    def __str__(self):
        return self.name


class Exam(models.Model):
    name = models.CharField(max_length=200)
    local_name = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    description = models.CharField(max_length=2000)
    duration = models.IntegerField()
    category = models.ForeignKey(ExamCategory)


    def score(self):
        return self.question_set.aggregate(Sum('score'))['score__sum']


    def __str__(self):
        return str(self.pk) + " " + self.name


class RequiredKnowledge(models.Model):
    name = models.CharField(max_length=200)
    exams = models.ManyToManyField(Exam, related_name='required_knowledge')

    def __str__(self):
        return self.name


def update_image_name(instance, filename):
    return os.path.join(
        os.path.join(os.path.normpath(force_text(datetime.datetime.now().strftime(force_str('question/images')))),
                     str(instance.id)) + '.png')


class Question(models.Model):
    text = models.CharField(max_length=500)
    exam = models.ForeignKey(Exam)
    score = models.IntegerField(default=1)
    code = models.CharField(max_length=2000, null=True, blank=True)
    image = models.FileField(upload_to=update_image_name, null=True, blank=True)


    def number_of_answers(self):
        return self.choice_set.filter(answer=True).aggregate(Count('answer'))['answer__count']


    def __str__(self):
        return str(self.id)


class Choice(models.Model):
    text = models.CharField(max_length=200)
    question = models.ForeignKey(Question)
    answer = models.BooleanField(default=False)

    def __str__(self):
        return str(self.pk)




