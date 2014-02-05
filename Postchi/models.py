from django.db import models
from django.contrib.auth.models import User

class ConfirmMail(models.Model):
    user = models.ForeignKey(User)
    send_date = models.DateTimeField()
    confirm_key = models.CharField(max_length=20)

