from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from exam.models import Question, Exam, Choice


class ExamAnswer(models.Model):
    user = models.ForeignKey(User)
    exam = models.ForeignKey(Exam)
    score = models.IntegerField(default=0)

    def __unicode__(self):
        return self.user.get_full_name() + " on exam: " + self.exam.local_name + " score:" + str(self.score)


class ExamAnswerHistory(models.Model):
    user = models.ForeignKey(User)
    exam = models.ForeignKey(Exam)

    def score(self):
        result = 0
        for answer in list(self.answers.all()):
            result += answer.catched_score()
        return result


class Answer(models.Model):
    question = models.ForeignKey(Question)
    exam_answer = models.ForeignKey(ExamAnswerHistory, related_name='answers')
    selected_choices = models.ManyToManyField(Choice, related_name='cho+')

    def catched_score(self):
        if self.is_true():
            return self.question.score
        else:
            return 0

    def is_true(self):
        if list(self.selected_choices.all()) == list(self.question.choice_set.filter(answer=True)):
            return True
        else:
            return False
