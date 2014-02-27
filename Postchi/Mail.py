import Postchi.models
from django.conf import settings as projSetting
from Postchi import settings as appSetting
from django.template import Context, Template
from django.template import loader
from Postchi.models import ConfirmMail
from Postchi.exceptions import *
from datetime import *

from django.core.mail import send_mail, EmailMessage

__author__ = 'Mahdi'


def send_confirm_mail(targetUser):
    import random, string

    def check_older_mails():
        return ConfirmMail.objects.filter(user=targetUser).first()

    def key_generator(size=25, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))

    def link_generator(key):
        return '{}/user/confirm/{}'.format(projSetting.SERVER_BASE_ADDRESS, key)

    old_mail = check_older_mails()
    if old_mail is None:
        user_key = key_generator(appSetting.CONFIRM_KEY_LENGTH)
        new_confirm_mail = ConfirmMail(user=targetUser, send_date=datetime.now(), confirm_key=user_key)
        new_confirm_mail.save()
    else:
        if appSetting.TIME_GAP != 0 & (datetime.now() - old_mail.send_date).total_seconds() < appSetting.TIME_GAP:
            raise TimeLimitBetweenTwo(
                remaining_time=appSetting.TIME_GAP - (datetime.now() - old_mail.send_date).total_seconds())
        user_key = old_mail.key

    mail_vars = Context(# mail body variables
        {
            'username': targetUser.username,
            'activate_link': projSetting.SERVER_BASE_ADDRESS+'user/confirm/'+str(targetUser.id)+'-'+user_key,
        }
    )
    confirm_template = loader.get_template('confirm_mail.html')
    mail_content = confirm_template.render(mail_vars)
    try:
        msg = EmailMessage('{}Confirm Your Azma-Web Account'.format(projSetting.EMAIL_SUBJECT_PREFIX),
                           mail_content,
                           projSetting.DEFAULT_FROM_EMAIL,
                           [targetUser.email])
        msg.content_subtype = "html"  # Main content is now text/html
        msg.send()
        # send_mail(
        #     '{}Confirm Your Azma-Web Account'.format(projSetting.EMAIL_SUBJECT_PREFIX), # Subject
        #     mail_content, # Body
        #     projSetting.DEFAULT_FROM_EMAIL, # From
        #     [targetUser.email]    # To
        # )
    except Exception as e:
        print (e.message)
        print("MAIL NOT SENT :-( ")
