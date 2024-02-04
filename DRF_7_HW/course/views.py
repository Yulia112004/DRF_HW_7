from rest_framework.viewsets import ModelViewSet
from course.models import Course
from course.serializers import CourseSerializer


class CourseViewSet(ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()