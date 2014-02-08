from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
import logging
from Postchi.models import ConfirmMail

from exam.models import Exam


def index(request):
    all_exams = Exam.objects.all()

    template = loader.get_template('sample.html')
    context = RequestContext(request, {'all_exams': all_exams})
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






