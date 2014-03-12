from django.db import models


class ExamCategory(models.Model):
    name = models.CharField(max_length=200)
    local_name = models.CharField(max_length=200)
    parent = models.ForeignKey("self", null=True, related_name='sub_categories')


    def number_of_exams(self):
        return self.exam_set.count()


class Exam(models.Model):
    name = models.CharField(max_length=200)
    local_name = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    description = models.CharField(max_length=2000)
    duration = models.IntegerField()

    category = models.ForeignKey(ExamCategory)


    def __str__(self):
        return str(self.pk) + " " + self.name


class RequiredKnowledge(models.Model):
    name = models.CharField(max_length=200)
    exams = models.ManyToManyField(Exam, related_name='required_knowledge')

    def __str__(self):
        return self.name


class Question(models.Model):
    text = models.CharField(max_length=500)
    exam = models.ForeignKey(Exam)
    score = models.IntegerField(default=1)

    def __str__(self):
        return self.text


class Choice(models.Model):
    text = models.CharField(max_length=200)
    question = models.ForeignKey(Question)
    answer = models.BooleanField(default=False)

    def __str__(self):
        return str(self.pk) + " " + self.text




