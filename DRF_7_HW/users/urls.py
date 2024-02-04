from users.apps import UsersConfig
from rest_framework.routers import DefaultRouter
from django.urls import path

from users.views import UserViewSet, UserUpdateAPIView

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r'user', UserViewSet, basename='user')

urlpatterns = [
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='user_update'),
] + router.urls