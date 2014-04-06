from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.db.models import Count
from django.http.response import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.template.context import RequestContext
from answer.models import ExamAnswerHistory, Answer, ExamAnswer
from answer.validator import validate_number_of_attempts
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
            if not validate_number_of_attempts(request.user.id, exam_id):
                return HttpResponse("Noch Noch")

            exam_answer = ExamAnswer.objects.get(user_id=request.user.id, exam_id=exam_id)

            context = RequestContext(request, {'answer': exam_answer})
            return HttpResponse(template.render(context))
        except ObjectDoesNotExist as e:
            return HttpResponseRedirect(reverse('exam:home'))
    if request.method == "POST":
        exam = Exam.objects.get(id=exam_id)
        exam_answer, is_new = ExamAnswer.objects.get_or_create(user_id=request.user.id, exam_id=exam_id)
        if not validate_number_of_attempts(request.user.id, exam_id):
            return HttpResponse("Noch Noch")

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




