from django.conf import settings
from django.db import connection
from django.test import TestCase
from exam.models import Exam, MultipleChoice
from datetime import datetime


class APITesting(TestCase):
    settings.DEBUG = True

    def test_to_find_an_exam_with_all_its_questions(self):
        e = Exam()
        e.name = "Simple Exam"
        e.start_date = datetime.now()
        e.save()
        q = e.question_set.create()
        choice1 = MultipleChoice()
        choice1.valid = True
        choice1.text = "RED"
        q.choice_set.add(choice1)
        print(choice1.id)
        self.assertIsNotNone(choice1.id)


    def test_2(self):
        print('bilbil')
        e = Exam.objects.all()
        self.assertIsNotNone(e.all())






