import os
import datetime

from django.db import models
from django.db.models import Sum, Count
from django.utils.encoding import force_text, force_str
from elephantblog.models import Entry
from feincms.content.comments.models import CommentsContent
from feincms.content.medialibrary.models import MediaFileContent
from feincms.content.richtext.models import RichTextContent
from django_enumfield import enum


class ExamCategory(models.Model):
    
    name = models.CharField(max_length=200)
    local_name = models.CharField(max_length=200)
    parent = models.ForeignKey("self", null=True, blank=True, related_name='sub_categories')


    def number_of_exams(self):
        return self.exam_set.count()

    def __str__(self):
        return self.name


class ExamState(enum.Enum):
    PENDING = 0
    PUBLISHED = 1
    FINISHED = 2
    labels = {
        PENDING: 'Pending',
        PUBLISHED: 'Published',
        FINISHED: 'Finished',
    }


class Exam(models.Model):
    name = models.CharField(max_length=200)
    local_name = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
    description = models.CharField(max_length=2000)
    duration = models.IntegerField()
    category = models.ForeignKey(ExamCategory)
    number_of_attempts = models.IntegerField(default=1)
    exam_state = enum.EnumField(ExamState, default=ExamState.PENDING)


    def score(self):
        score = self.question_set.aggregate(Sum('score'))['score__sum']
        if score is None:
            return 0
        else:
            return score


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


class Choice(models.Model):
    text = models.CharField(max_length=200)
    question = models.ForeignKey(Question)
    answer = models.BooleanField(default=False)

    def __str__(self):
        return str(self.pk)


# Entry.register_extensions('feincms.module.extensions.datepublisher',
# 'feincms.module.extensions.translations',
#                           'elephantblog.extensions.blogping',
# )
#
# Page.register_extensions(
#     'feincms.module.page.extensions.sites',
#     'feincms.module.page.extensions.titles',
# )
#
# Entry.register_extensions('feincms.module.extensions.datepublisher',
#                           # 'feincms.module.extensions.translations',
#                           'elephantblog.extensions.blogping',
#
#                           'feincms.module.extensions.seo',
# )
#
Entry.register_regions(
    ('main', 'Main content area'),
    ('header', 'Header content area')
)
Entry.create_content_type(RichTextContent,
                          regions=('main', 'sidebar',))
#
Entry.create_content_type(MediaFileContent, TYPE_CHOICES=(
    ('default', 'default'),
))

Entry.create_content_type(CommentsContent)