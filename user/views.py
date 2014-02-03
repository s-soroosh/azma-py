
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader, RequestContext
from azma import settings
from user.login import auth_user
from django.utils.translation import ugettext_lazy as _


def user_login(request):
    if request.method == "POST":
        return auth_user(request)

    if request.method == "GET":
        if request.user.is_authenticated():
            return HttpResponse("You have been authenticated before!")
        template = loader.get_template('login.html')
        context = RequestContext(request)
        return HttpResponse(template.render(context))

    return HttpResponse("Wrong Method!")


def user_logout(request):
    logout(request)


def user_register(request):
    registerTemplate = loader.get_template('register.html')
    if request.method == "POST":
        name = request.POST["name"]
        last_name = request.POST["lastName"]
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password"]

        u = User(username=username, password=password, first_name=name, last_name=last_name, email=email)
        try:
            u.full_clean()
        except ValidationError as e:
            context = RequestContext(request, {'validation_error': e})
            return HttpResponse(registerTemplate.render(context))
        u.save()
        context = RequestContext(request,
                                 {'redirect_url': settings.DEFAULT_LOGIN_URL,
                                  'message': _("You have been registered successfully")})
        return HttpResponse(registerTemplate.render(context))
    else:
        context = RequestContext(request)
        return HttpResponse(registerTemplate.render(context))