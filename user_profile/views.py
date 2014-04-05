from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.http.response import HttpResponse
from django.template import loader
from django.template.context import RequestContext
from django.utils.translation import ugettext_lazy as _
from answer.models import ExamAnswerHistory
from exam.models import ExamCategory, Exam

profile_template = loader.get_template('profile.html')


@login_required(login_url='/user/login')
def show_profile(request):
    profile_template = loader.get_template('profile.html')
    exam_answers = ExamAnswerHistory.objects.filter(user__id=request.user.id)
    exam_categories = list(ExamCategory.objects.filter(exam__examanswer__user=1))

    for category in exam_categories:
        category.answers = list(ExamAnswerHistory.objects.filter(user__id=request.user.id).filter(exam__category=category.id))
        category.sum_score = 0
        for answer in category.answers:
            category.sum_score += answer.score()

    sum_score = 0
    for a in exam_answers:
        sum_score += a.score()
    context = RequestContext(request,
                             {'sum_score': sum_score, 'exam_categories': exam_categories, 'exam_answers': exam_answers})
    return HttpResponse(profile_template.render(context))


@login_required(login_url='/user/login')
def change_password(request):
    if request.method == "POST":
        oldPass = request.POST["oldPass"]
        newPass = request.POST["newPass"]

        if request.user.check_password(oldPass):
            request.user.set_password(newPass)
            request.user.save()
            context = RequestContext(request, {'message': _('password has been changed')})

            return HttpResponse(profile_template.render(context))
        else:
            return HttpResponse("!!!!!")

    else:
        return HttpResponse(profile_template.render(RequestContext(request)))






