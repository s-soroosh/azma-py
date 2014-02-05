from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse

from exam.models import Exam


def index(request):
    all_exams = Exam.objects.all()

    template = loader.get_template('sample.html')
    context = RequestContext(request, {'all_exams': all_exams})
    return HttpResponse(template.render(context))


def intro(request, exam_id):
    if request.method == "GET":
        exam = Exam.objects.get(id=exam_id)
        template = loader.get_template('exam_intro.html')
        context = RequestContext(request, {'exam': exam})
        return HttpResponse(template.render(context))





