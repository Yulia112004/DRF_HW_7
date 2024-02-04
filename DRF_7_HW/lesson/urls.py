from django.urls import path
from lesson.apps import LessonConfig
from lesson.views import LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView

app_name = LessonConfig.name


urlpatterns = [
    path('', LessonListAPIView.as_view(), name='lessons'),
    path('create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson'),
    path('update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_delete'),
]