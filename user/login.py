from django.contrib.auth import authenticate, login
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader, RequestContext
from azma import settings
from django.utils.translation import ugettext_lazy as _
import multiprocessing

__author__ = 'soroosh'


def auth_user(request):
    multiprocessing.cpu_count()
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect(settings.DEFAULT_LOGIN_URL)
        else:
            template = loader.get_template('login.html')
            context = RequestContext(request, {'error_message': 'User is disabled'})
            return HttpResponse(template.render(context))

    else:
        template = loader.get_template('login.html')
        context = RequestContext(request, {'error_message': _('Username or password is wrong')})
        return HttpResponse(template.render(context))

