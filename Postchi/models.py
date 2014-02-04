from django.db import models
from django.contrib.auth.models import User
class Mail(models.Model):
    user = models.ForeignKey(User)
    send_date= models.DateTimeField()
    mail_type=models.ForeignKey(MailType)
    mail_status=models.SmallIntegerField()

class MailType(models.Model):
    name = models.CharField(max_length=50)

