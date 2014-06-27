from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.template.context import RequestContext
from django.views.generic import View


class TutorialView(View):
    def get(self, request):
        template = loader.get_template('tutorial_page.html')
        context = RequestContext(request)
        return HttpResponse(template.render(context))