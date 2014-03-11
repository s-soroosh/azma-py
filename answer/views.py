# Create your views here.
from django.http.response import HttpResponse
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
        exam_answer = ExamAnswer.objects.get(user_id=request.user.id, exam_id=exam_id)
        context = RequestContext(request, {'answer': exam_answer})
        return HttpResponse(template.render(context))
    if request.method == "POST":
        if ExamAnswer.objects.filter(user_id=request.user.id, exam_id=exam_id).exists():
            return HttpResponse(
                template.render(RequestContext(request, {'error_message': _('You have done this exam')})))

    exam = Exam.objects.get(id=exam_id)
    exam_answer = ExamAnswer()
    exam_answer.user_id = request.user.id
    exam_answer.exam = exam
    exam_answer.save()
    for q in exam.question_set.all():
        if str(q.id) in request.POST.keys():
            answer = Answer()
            answer.question = q
            answer.exam_answer = exam_answer
            answer.save()
            # exam_answer.answers.add(answer)
            # answer.selected_choices.
            print(q.text)
            for a in request.POST.getlist(str(q.id)):
                answer.selected_choices.add(a)
                print("result: %s" % q.choice_set.get(id=str(a)))

    context = RequestContext(request, {'answer': exam_answer})
    return HttpResponse(template.render(context))




