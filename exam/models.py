from django.db import models


class Exam(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    start_date = models.DateTimeField()

    def __str__(self):
        return self.name;