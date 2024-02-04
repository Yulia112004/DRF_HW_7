from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from course.models import Course
from course.permission import IsOwner
from lesson.permission import IsStaff
from course.serializers import CourseSerializer


class CourseViewSet(ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    queryset = Course.objects.all()

    def get_permissions(self):
        if self.action == 'retrieve':
            permission_classes = [IsOwner | IsStaff]
        elif self.action == 'create':
            permission_classes = [IsStaff]
        elif self.action == 'destroy':
            permission_classes = [IsOwner | IsStaff]
        elif self.action == 'update':
            permission_classes = [IsOwner | IsStaff]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]