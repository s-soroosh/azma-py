from django.http import HttpResponse
from django.template import loader
from django.template.context import RequestContext
from django.views.generic import View
from django.db.models import Count
from tutorial.models import TutorialCategory, Tutorial, TutorialExam, TutorialExamAnswer, TutorialExamAnswerHistory, TutorialAnswer
from django.http.response import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.sites.models import Site
from azma.settings import SERVER_BASE_ADDRESS
from django.utils.functional import *

class TutorialView(View):
    def get(self, request):
        categories = TutorialCategory.objects.filter(parent_id=None)
        latest_tutorials = Tutorial.objects.all().order_by('-registered_date').all()[:5]

        template = loader.get_template('tutorial_page.html')

        context = RequestContext(request, {'latest_tutorials': latest_tutorials, 't_categories': categories})
        return HttpResponse(template.render(context))


class TutorialWithCategoryView(View):
    def get(self, request, category_name):
        categories = TutorialCategory.objects.filter(parent_id=None)
        t_category = TutorialCategory.objects.get(name=category_name.upper())
        category = t_category
        latest_tutorials = Tutorial.objects.all().order_by('-registered_date').all()[:5]
        while category.parent is not None:
            category = category.parent
        template = loader.get_template('category_detail.html')

        context = RequestContext(request,
                                 {'latest_tutorials': latest_tutorials, 'category': category, 't_category': t_category,
                                  't_categories': categories})
        return HttpResponse(template.render(context))


class TutorialDetailView(View):
    def get(self, request, tutorial_name):
        categories = TutorialCategory.objects.filter(parent_id=None)
        tutorial = Tutorial.objects.get(name=tutorial_name.upper())
        latest_tutorials = Tutorial.objects.all().order_by('-registered_date').all()[:5]
        path = SERVER_BASE_ADDRESS
        category = tutorial.category
        while category.parent is not None:
            category = category.parent
        template = loader.get_template('tutorial_detail.html')
        context = RequestContext(request,
                                 {'latest_tutorials': latest_tutorials, 'category': category, 'tutorial': tutorial,
                                  't_categories': categories, 'path': path, })
        return HttpResponse(template.render(context))


class TutorialAnswerAnalyze(View):
    def post(self, request, exam_tu_id):
        tutorial_exam = TutorialExam.objects.get(pk=exam_tu_id)
        exam_answer, is_new = TutorialExamAnswer.objects.get_or_create(user_id=request.user.id, exam_tutorial_id=exam_tu_id)
        exam_answer_history = TutorialExamAnswerHistory()
        exam_answer_history.user_id = request.user.id
        exam_answer_history.exam_answers = tutorial_exam
        exam_answer_history.save()
        for q in tutorial_exam.questions.all():
            answer = TutorialAnswer()
            answer.tutorial_question = q
            answer.tutorial_exam_answer = exam_answer_history
            answer.save()

            if str(q.id) in request.POST.keys():
                for a in request.POST.getlist(str(q.id)):
                    answer.selected_answer_choices.add(a)

            else:
                answer.selected_answer_choices.add(-1)

        total_score = 0
        for i in tutorial_exam.questions.all():
            total_score += i.score
        exam_answer.max_score = total_score
        exam_answer.save()

        if exam_answer_history.score() > exam_answer.score:
            exam_answer.score = exam_answer_history.score()
            exam_answer.save()
        template = loader.get_template('quiz_answer.html')
        context = RequestContext(request, {'tu_answer': exam_answer_history, })
        return HttpResponse(template.render(context))


class TutorialExamView(View):
    def get(self, request, tutorial_id):
        tutorial_exam = TutorialExam.objects.get(pk=tutorial_id)
        exam_answer = TutorialExamAnswer.objects.get(user_id=request.user.id, exam_tutorial_id=tutorial_id)

        total_score = 0
        for i in tutorial_exam.questions.all():
            total_score += i.score
        tutorial_exam.max_score = total_score
        tutorial_exam.save()
        template = loader.get_template('tutorial_exam.html')
        context = RequestContext(request, {'exam': tutorial_exam, 'answer': exam_answer, })
        return HttpResponse(template.render(context))
