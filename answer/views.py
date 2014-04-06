from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.db.models import Count
from django.http.response import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.template.context import RequestContext
from answer.models import ExamAnswerHistory, Answer, ExamAnswer
from exam.models import Exam
from django.db import transaction
from django.utils.translation import ugettext_lazy as _


@transaction.atomic()
def analyze_answer(request, exam_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('exam:home'))
    template = loader.get_template('answer.html')
    if request.method == "GET":
        try:
            attempts = \
                ExamAnswerHistory.objects.filter(user_id=request.user.id, exam_id=exam_id).aggregate(Count('id'))[
                    'id__count']
            exam = Exam.objects.get(id=exam_id)
            if attempts == exam.number_of_attempts:
                return HttpResponse("Noch Noch")

            exam_answer = ExamAnswer.objects.get(user_id=request.user.id, exam_id=exam_id)

            context = RequestContext(request, {'answer': exam_answer})
            return HttpResponse(template.render(context))
        except ObjectDoesNotExist as e:
            return HttpResponseRedirect(reverse('exam:home'))
    if request.method == "POST":
        exam = Exam.objects.get(id=exam_id)
        exam_answer = ExamAnswer.objects.get_or_create(user_id=request.user.id, exam_id=exam_id)[0]
        if ExamAnswerHistory.objects.filter(user_id=request.user.id, exam_id=exam_id).exists():
            attempts = \
                ExamAnswerHistory.objects.filter(user_id=request.user.id, exam_id=exam_id).aggregate(Count('id'))[
                    'id__count']

            if attempts == exam.number_of_attempts:
                return HttpResponse("Noch Noch")

                # exam_answer = ExamAnswerHistory.objects.filter(user_id=request.user.id, exam_id=exam_id).aggregate(Count('id'))['id__count']
                # return HttpResponse(
                #     template.render(
                #         RequestContext(request, {'answer': exam_answer, 'error_message': _('You have done this exam')})))

        exam_answer_history = ExamAnswerHistory()
        exam_answer_history.user_id = request.user.id
        exam_answer_history.exam = exam
        exam_answer_history.save()
        for q in exam.question_set.all():
            answer = Answer()
            answer.question = q
            answer.exam_answer = exam_answer_history
            answer.save()
            if str(q.id) in request.POST.keys():
                for a in request.POST.getlist(str(q.id)):
                    answer.selected_choices.add(a)
            else:
                answer.selected_choices.add(-1)

        if exam_answer_history.score() > exam_answer.score:
            exam_answer.score = exam_answer_history.score()
            exam_answer.save()

    context = RequestContext(request, {'answer': exam_answer_history})
    return HttpResponse(template.render(context))




