from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
import logging
from Postchi.models import ConfirmMail

from exam.models import Exam, ExamCategory


def what(request):
    template = loader.get_template('intro.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))


def intro(request, exam_id):
    if request.method == "GET":
        try:
            exam = Exam.objects.get(id=exam_id)
            template = loader.get_template('exam_intro.html')
            from django.utils import timezone

            context = RequestContext(request, {'exam': exam, 'current_date': timezone.now()})
            return HttpResponse(template.render(context))
        except ObjectDoesNotExist as e:
            return HttpResponseRedirect(reverse('exam:home'))


def sub_categories(request, category_id):
    sub_categories = ExamCategory.objects.filter(parent__id=category_id)
    template = loader.get_template('sub_categories.html')
    context = RequestContext(request, {'sub_categories': sub_categories})
    return HttpResponse(template.render(context))


def start(request, exam_id):
    if (request.method == "GET"):
        exam = Exam.objects.get(id=exam_id)
        template = loader.get_template('start.html')
        context = RequestContext(request, {'exam': exam})
        return HttpResponse(template.render(context))
    else:
        print("phohdj cedioj ")

        exam = Exam.objects.get(id=exam_id)
        for q in exam.question_set.all():
            if str(q.id) in request.POST.keys():
                print(q.text)
                for answer in request.POST.getlist(str(q.id)):
                    print("result: %s" % q.choice_set.get(id=str(answer)))


def index(request):
    template = loader.get_template('home.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))