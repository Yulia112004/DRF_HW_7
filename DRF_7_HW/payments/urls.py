from django.urls import path
from payments.views import PaymentListAPIView, PaymentCreateAPIView
from payments.apps import PaymentsConfig


app_name = PaymentsConfig.name

urlpatterns = [
    path('', PaymentListAPIView.as_view(), name='payments'),
    path('create/', PaymentCreateAPIView.as_view(), name='payments_create'),
]