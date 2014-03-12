from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.template import loader
from django.template.context import RequestContext
from django.utils.translation import ugettext_lazy as _
from answer.models import ExamAnswer
from exam.models import ExamCategory, Exam

profile_template = loader.get_template('profile.html')


@login_required(login_url='/user/login')
def show_profile(request):
    profile_template = loader.get_template('profile.html')
    # Exam().examanswer_set
    exam_answers = ExamAnswer.objects.filter(user__id=request.user.id)
    sum_score = 0
    for a in exam_answers:
        sum_score += a.score()
    context = RequestContext(request, {'sum_score': sum_score, 'exam_answers': exam_answers})
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






