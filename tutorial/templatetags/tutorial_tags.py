from tutorial.models import TutorialCategory

__author__ = 'soroosh'

from django import template

register = template.Library()


class TutorialCategoryNode(template.Node):
    def __init__(self, cats):
        self.cats = cats

    def render(self, context):
        context['t_categories'] = self.cats


@register.assignment_tag
def tutorial_categories():
    categories = TutorialCategory.objects.filter(parent__name=None)
    return categories.all()




