import os
import datetime

from django.contrib.auth.models import User
from django.db import models
from jdatetime import datetime as jalali_datetime
from tinymce.models import HTMLField
from django_enumfield import enum
from django.db.models import Sum, Count
from django.utils.encoding import force_text, force_str


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
        ordering = ['registered_date']

    category = models.ForeignKey(TutorialCategory, related_name='tutorials')
    keyword = models.CharField(max_length=200)  # comma separated
    abstract = models.TextField()
    name = models.CharField(max_length=120, primary_key=True)
    local_name = models.CharField(max_length=150)
    author = models.ForeignKey(User)
    content = models.TextField()
    registered_date = models.DateTimeField()

    def get_persian_registered_date(self):
        return jalali_datetime.fromgregorian(datetime=self.registered_date).strftime('%Y/%m/%d')

    def __unicode__(self):
        return self.local_name


class TutorialExamState(enum.Enum):
    PENDING = 0
    PUBLISHED = 1
    FINISHED = 2
    labels = {
        PENDING: 'Pending',
        PUBLISHED: 'Published',
        FINISHED: 'Finished',
    }


class TutorialExam(models.Model):
    tutorial = models.OneToOneField(Tutorial, related_name='exam', primary_key=True)
    local_name = models.CharField(max_length=150)
    content = HTMLField()
    max_score = models.IntegerField(default=0)

    def score(self):
        score = self.question_set.aggregate(Sum('score'))['score__sum']
        if score is None:
            return 0
        else:
            return score

    def __unicode__(self):
        return self.local_name


def update_image_name(instance, filename):
    return os.path.join(
        os.path.join(os.path.normpath(force_text(datetime.datetime.now().strftime(force_str('question/images')))),
                     str(instance.id)) + '.png')


class TutorialQuestion(models.Model):
    text = models.CharField(max_length=500)
    exam = models.ForeignKey(TutorialExam, related_name="questions")
    score = models.IntegerField(default=1)
    code = models.TextField(null=True, blank=True)
    image = models.FileField(upload_to=update_image_name, null=True, blank=True)
    # according to this doc : https://docs.djangoproject.com/en/1.7/ref/models/fields/
    JAVA = "java"
    JS = "javascript"
    PHP = "PHP"
    LANGUAGES = (
        (JAVA, "Java"),
        (JS, "Javascript"),
        (PHP, "PHP")
    )
    code_type = models.CharField(max_length=15, choices=LANGUAGES, default=JAVA)

    def number_of_answers(self):
        return self.choice_set.filter(answer=True).aggregate(Count('answer'))['answer__count']

    def __str__(self):
        return str(self.id)


class TutorialChoice(models.Model):
    text = models.CharField(max_length=200)
    question = models.ForeignKey(TutorialQuestion, related_name="choice")
    answer = models.BooleanField(default=False)

    def __str__(self):
        return str(self.pk)


class TutorialExamAnswer(models.Model):
    user = models.ForeignKey(User)
    exam_tutorial = models.ForeignKey(TutorialExam)
    score = models.IntegerField(default=0)
    max_score = models.IntegerField(default=0)

    def __unicode__(self):
        return self.user.get_full_name() + " on exam: " + self.exam_tutorial.local_name


class TutorialExamAnswerHistory(models.Model):
    user = models.ForeignKey(User)
    exam_answers = models.ForeignKey(TutorialExam)

    def score(self):
        result = 0
        for answer in list(self.answers.all()):
            result += answer.catched_score()
        return result


class TutorialAnswer(models.Model):
    tutorial_question = models.ForeignKey(TutorialQuestion)
    tutorial_exam_answer = models.ForeignKey(TutorialExamAnswerHistory, related_name='answers')
    selected_answer_choices = models.ManyToManyField(TutorialChoice, related_name='ans+')

    def catched_score(self):
        if self.is_true():
            return self.tutorial_question.score
        else:
            return 0

    def is_true(self):
        if list(self.selected_answer_choices.all()) == list(self.tutorial_question.choice.filter(answer=True)):
            return True
        else:
            return False

