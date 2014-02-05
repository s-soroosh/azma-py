import Postchi.models
from azma import settings as projSetting
from Postchi import settings as appSetting
from django.template import Context, Template
from django.template.loader import render_to_string
from Postchi.models import ConfirmMail,WelcomeMail
from Postchi.exceptions import *
from datetime import *


from django.core.mail import send_mail

__author__ = 'Mahdi'

def send_confirm_mail(target_user):
    import random, string

    def check_older_mails():
        return ConfirmMail.objects.filter(user=target_user).first()

    def key_generator(size=25, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))

    def link_generator(key):
        return '{}/user/confirm/{}'.format(projSetting.SERVER_BASE_ADDRESS, key)

    old_mail = check_older_mails()
    if old_mail is None:
        user_key = key_generator(appSetting.CONFIRM_KEY_LENGTH)
        new_confirm_mail = ConfirmMail(user=target_user, send_date=datetime.now(),confirm_key= user_key)
        new_confirm_mail.save()
    else:
        if appSetting.TIME_GAP != 0 & (datetime.now()-old_mail.send_date).total_seconds() < appSetting.TIME_GAP :
            raise TimeLimitBetweenTwo(remaining_time=appSetting.TIME_GAP - (datetime.now() - old_mail.send_date).total_seconds())
        user_key = old_mail.key

    mail_vars = Context(  # mail body variables
        {
            'username': target_user.username,
            'activate_key': user_key,
        }
    )
    mail_content = render_to_string('Confirm.html', mail_vars)
    try:
        send_mail(
            '{}Confirm Your Azma-Web Account'.format(projSetting.EMAIL_SUBJECT_PREFIX),  # Subject
            mail_content,   # Body
            projSetting.DEFAULT_FROM_EMAIL,   # From
            [target_user.email]    # To
        )
    except:
        print("MAIL NOT SENT :-( ")


def send_welcome_mail(target_user):
    welcome_mail = WelcomeMail(user=target_user, send_date=datetime.now())
    welcome_mail.save()
    mail_vats =Context({'profile_link':'{}/user/profile'.format(projSetting.SERVER_BASE_ADDRESS)})
    mail_content = render_to_string('Welcome.html',Context)
    try:
        send_mail(
            '{}Welcome to AzmaWeb'.format(projSetting.EMAIL_SUBJECT_PREFIX),  # Subject
            mail_content,   # Body
            projSetting.DEFAULT_FROM_EMAIL,   # From
            [target_user.email]    # To
        )
    except:
        print("MAIL NOT SENT :-( ")
