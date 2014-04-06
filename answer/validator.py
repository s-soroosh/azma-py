from django.db.models import Count
from answer.models import ExamAnswerHistory
from exam.models import Exam


def validate_number_of_attempts(user_id,exam_id):
    attempts = \
        ExamAnswerHistory.objects.filter(user_id=user_id, exam_id=exam_id).aggregate(Count('id'))[
            'id__count']


    exam = Exam.objects.get(id=exam_id)
    if attempts >= exam.number_of_attempts:
        return False

    return True