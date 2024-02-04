from django.urls import path

from course.apps import CourseConfig
from rest_framework.routers import DefaultRouter
from course.views import CourseViewSet
from course.views import CourseViewSet, SubscriptionCreateAPIView, SubscriptionDestroyAPIView

app_name = CourseConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
    path('course/<int:pk>/subscribe/', SubscriptionCreateAPIView.as_view(), name='subscribe'),
    path('course/<int:pk>/unsubscribe/', SubscriptionDestroyAPIView.as_view(), name='unsubscribe'),
] + router.urls