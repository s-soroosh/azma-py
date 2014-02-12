from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.template import loader
from django.template.context import RequestContext


@login_required(login_url='/user/login')
def show_profile(request):
    template = loader.get_template('profile.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))
