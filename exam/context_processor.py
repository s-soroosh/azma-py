__author__ = 'soroosh'


def categories(request):
    return {'categories': request.categories}
