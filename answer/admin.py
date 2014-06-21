# from answer.models import ExamAnswer, ExamAnswerHistory, Answer

# __author__ = 'soroosh'
#
# from django.contrib import admin
#
# admin.site.register(ExamAnswer)
# admin.site.register(Answer)
# admin.site.register(ExamAnswerHistory)


from random import sample



for a in range(100):
    print str(a) +"time result: "+ str(sample(['a','b','c','d'],2))
