__author__ = 'soroosh'


def categories(request):
     # return {'categories': None}
     return {'categories': request.categories}
