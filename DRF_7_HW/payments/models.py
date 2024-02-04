from django.conf import settings
from django.db import models

from course.models import Course
from lesson.models import Lesson
from users.models import NULLABLE


class Payment(models.Model):
    CASH = 'cash'
    TRANSFER = 'transfer'
    PAYMENT_METHOD = (
        (CASH, 'Наличными'),
        (TRANSFER, 'Перевод на счет')
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='пользователь',
                             **NULLABLE,  related_name='payment')
    date = models.DateField(auto_now=True, verbose_name='дата оплаты')
    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='оплаченный курс', **NULLABLE)
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='оплаченный урок', **NULLABLE)
    payment_amount = models.PositiveIntegerField(verbose_name='сумма оплаты')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD, verbose_name='способ оплаты')

    def __str__(self):
        return f'{self.user} - {self.payment_amount} ({self.payment_method})'

    class Meta:
        verbose_name = 'платёж'
        verbose_name_plural = 'платежи'