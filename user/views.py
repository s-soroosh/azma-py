from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader, RequestContext
from user.login import auth_user


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
    if request.method == "POST":
        name = request.POST["name"]
        last_name = request.POST["lastName"]
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password"]

        u = User(username=username, password=password, first_name=name, last_name=last_name, email=email)
        u.save()
        return HttpResponse("User has been registered!")
    else:
        template = loader.get_template('register.html')
        context = RequestContext(request)
        return HttpResponse(template.render(context))