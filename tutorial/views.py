from django.http import HttpResponse
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


class TutorialWithCategoryView(View):
    def get(self, request, category_name):

        t_category = TutorialCategory.objects.get(name=category_name.upper())
        template = loader.get_template('category_detail.html')

        context = RequestContext(request, {'t_category': t_category})
        return HttpResponse(template.render(context))
