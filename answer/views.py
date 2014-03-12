from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http.response import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.template.context import RequestContext
from answer.models import ExamAnswer, Answer
from exam.models import Exam
from django.db import transaction
from django.utils.translation import ugettext_lazy as _


@transaction.atomic()
def analyze_answer(request, exam_id):
    template = loader.get_template('answer.html')
    if request.method == "GET":
        try:
            exam_answer = ExamAnswer.objects.get(user_id=request.user.id, exam_id=exam_id)
            context = RequestContext(request, {'answer': exam_answer})
            return HttpResponse(template.render(context))
        except ObjectDoesNotExist as e:
            return HttpResponseRedirect(reverse('exam:home'))
    if request.method == "POST":
        if ExamAnswer.objects.filter(user_id=request.user.id, exam_id=exam_id).exists():
            exam_answer = ExamAnswer.objects.get(user_id=request.user.id, exam_id=exam_id)
            return HttpResponse(
                template.render(
                    RequestContext(request, {'answer': exam_answer, 'error_message': _('You have done this exam')})))

        exam = Exam.objects.get(id=exam_id)
        exam_answer = ExamAnswer()
        exam_answer.user_id = request.user.id
        exam_answer.exam = exam
        exam_answer.save()
        for q in exam.question_set.all():
            answer = Answer()
            answer.question = q
            answer.exam_answer = exam_answer
            answer.save()
            if str(q.id) in request.POST.keys():
                for a in request.POST.getlist(str(q.id)):
                    answer.selected_choices.add(a)
            else:
                answer.selected_choices.add(-1)
    context = RequestContext(request, {'answer': exam_answer})
    return HttpResponse(template.render(context))




