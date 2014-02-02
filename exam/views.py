from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse
from exam.models import Exam


def index(request):
    all_exams = Exam.objects.all()

    template = loader.get_template('sample.html')
    context = RequestContext(request, {'all_exams': all_exams})
    return HttpResponse(template.render(context))


