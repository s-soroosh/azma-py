from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.db.models import Count
from django.db.models.aggregates import Avg
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from answer.models import ExamAnswerHistory

from exam.models import Exam, ExamCategory


def what(request):
    template = loader.get_template('intro.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))


from django.utils import timezone


def intro(request, exam_id):
    if request.method == "GET":
        try:
            exam = Exam.objects.get(id=exam_id)
            template = loader.get_template('exam_intro.html')
            attempts = \
                ExamAnswerHistory.objects.filter(user_id=request.user.id, exam_id=exam_id).aggregate(Count('id'))[
                    'id__count']
            context = RequestContext(request, {'exam': exam, 'attempts': attempts, 'current_date': timezone.now()})
            return HttpResponse(template.render(context))
        except ObjectDoesNotExist as e:
            return HttpResponseRedirect(reverse('exam:home'))


def sub_categories(request, category_id):
    sub_categories = ExamCategory.objects.filter(parent__id=category_id)
    template = loader.get_template('sub_categories.html')
    context = RequestContext(request, {'sub_categories': sub_categories})
    return HttpResponse(template.render(context))


def start(request, exam_id):
    if request.method == "GET":
        exam = Exam.objects.get(id=exam_id)
        user_answers_count = \
            ExamAnswerHistory.objects.filter(exam_id=exam_id, user_id=request.user.id).aggregate(Count('id'))[
                'id__count']
        template = loader.get_template('start.html')
        participates_count = exam.examanswer_set.aggregate(Count('id'))['id__count']
        context = RequestContext(request, {'user_answers_count': user_answers_count, 'exam': exam,
                                           'participates_count': participates_count})
        return HttpResponse(template.render(context))
    else:
        return HttpResponse('% method is not permitted', request.method)


def index(request):
    template = loader.get_template('home.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))