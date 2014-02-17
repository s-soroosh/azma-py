from django.http import HttpResponse
from django.template import Template
from django.template import loader, RequestContext

__author__ = 'soroosh'

from django.shortcuts import render


def about(request):
    template = loader.get_template('about.html')
    context = RequestContext(request)

    return HttpResponse(template.render(context))



