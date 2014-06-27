from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.template.context import RequestContext
from django.views.generic import View
from tutorial.models import TutorialCategory


class TutorialView(View):
    def get(self, request):
        categories = TutorialCategory.objects.filter(parent_id=None)

        template = loader.get_template('tutorial_page.html')

        context = RequestContext(request, {'t_categories': categories})
        return HttpResponse(template.render(context))