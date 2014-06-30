from django.http import HttpResponse
from django.template import loader
from django.template.context import RequestContext
from django.views.generic import View

from tutorial.models import TutorialCategory, Tutorial


class TutorialView(View):
    def get(self, request):
        categories = TutorialCategory.objects.filter(parent_id=None)

        template = loader.get_template('tutorial_page.html')

        context = RequestContext(request, {'t_categories': categories})
        return HttpResponse(template.render(context))


class TutorialWithCategoryView(View):
    def get(self, request, category_name):
        categories = TutorialCategory.objects.filter(parent_id=None)
        t_category = TutorialCategory.objects.get(name=category_name.upper())
        category = t_category
        while category.parent is not None:
            category = category.parent
        template = loader.get_template('category_detail.html')

        context = RequestContext(request, {'category': category, 't_category': t_category, 't_categories': categories})
        return HttpResponse(template.render(context))


class TutorialDetailView(View):
    def get(self, request, tutorial_name):
        categories = TutorialCategory.objects.filter(parent_id=None)
        tutorial = Tutorial.objects.get(name=tutorial_name.upper())
        category = tutorial.category
        while category.parent is not None:
            category = category.parent
        template = loader.get_template('tutorial_detail.html')
        context = RequestContext(request, {'category': category, 'tutorial': tutorial, 't_categories': categories})
        return HttpResponse(template.render(context))
