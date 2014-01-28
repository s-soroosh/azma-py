from django.contrib.auth import authenticate, login
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.template import loader, RequestContext
from azma import settings

__author__ = 'soroosh'


def auth_user(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect(settings.DEFAULT_LOGIN_URL)
        else:
            template = loader.get_template('login.html')
            context = RequestContext(request)
            return HttpResponse(template.render(context, {'error_message': 'User is disabled'}))

    else:
        template = loader.get_template('login.html')
        context = RequestContext(request, {'error_message': 'User does not exist'})
        return HttpResponse(template.render(context))

