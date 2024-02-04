from rest_framework.pagination import PageNumberPagination

from course.models import Course
from lesson.models import Lesson


class CoursePaginator(PageNumberPagination):
    page_size = len(Course.objects.all())


class LessonPaginator(PageNumberPagination):
    page_size = len(Lesson.objects.all())