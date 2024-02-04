from rest_framework import serializers

from payments.serializers import PaymentSerializer
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    payments_count = serializers.SerializerMethodField()
    payments = PaymentSerializer(many=True, source='payment')

    def get_payments_count(self, instance):
        return instance.payment.count()
    class Meta:
        model = User
        fields = ('email', 'password', 'phone', 'city', 'avatar')
        fields = ('id', 'email', 'password', 'payments_count', 'payments', 'phone', 'city', 'avatar')