from django.contrib.auth import authenticate, login
from django.http import HttpRequest, HttpResponse

__author__ = 'soroosh'


def auth_user(request):

        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse("Valid user!")
            else:
                return HttpResponse("Disable!")
        else:
            return HttpResponse("Not authenticated")
