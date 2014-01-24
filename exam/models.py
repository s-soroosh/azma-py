from django.db import models


class Exam(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField()

    def __str__(self):
        return self.name;