from exam.models import ExamCategory

__author__ = 'soroosh'


class CommonObjectsMiddleware(object):
    counter = 0

    def process_request(self, request):
        self.counter += 1
        print("count: " + str(self.counter))
        all_categories = ExamCategory.objects.all()

        request.categories = list(all_categories)
        return None


