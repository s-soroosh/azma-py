from functools import wraps
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, RequestContext
from azma import settings
from user.login import auth_user



def is_user_anon(login_url=None):

    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated():
                return HttpResponseRedirect(settings.DEFAULT_LOGIN_URL)
            else:
                return view_func(request, *args, **kwargs)

        return _wrapped_view

    return decorator


@is_user_anon(login_url=settings.DEFAULT_LOGIN_URL)
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
    return HttpResponseRedirect(settings.DEFAULT_LOGIN_URL)


@is_user_anon(login_url=settings.DEFAULT_LOGIN_URL)
def user_register(request):
    register_template = loader.get_template('register.html')

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
            return HttpResponse(register_template.render(context))
        u.save()
        return HttpResponseRedirect(reverse('pending'))
    else:
        context = RequestContext(request)
        return HttpResponse(register_template.render(context))


@is_user_anon(login_url=settings.DEFAULT_LOGIN_URL)
def show_pending(request):
    pending_template = loader.get_template('pending_for_confirm.html')
    context = RequestContext(request)
    return HttpResponse(pending_template.render(context))