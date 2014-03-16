from exam.models import ExamCategory

__author__ = 'soroosh'


class CommonObjectsMiddleware(object):
    counter = 0

    def process_exception(self, a, b):
        print a
        print b
        pass

    def process_request(self, request):
        self.counter += 1
        print("count: " + str(self.counter))
        all_categories = ExamCategory.objects.filter(parent__isnull=True)

        request.categories = list(all_categories)
        return None


