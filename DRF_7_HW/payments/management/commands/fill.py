from django.core.management.base import BaseCommand

from course.models import Course
from lesson.models import Lesson
from payments.models import Payment
from users.models import User


class Command(BaseCommand):
    help = 'Команда для добавления данных в модель Payment'

    def handle(self, *args, **options):
        user = User.objects.get(email='byckova1@gmail.com')
        course = Course.objects.get(id=2)
        lesson = Lesson.objects.get(id=2)

        payment_amount = 300
        payment_method = 'transfer'

        payment = Payment.objects.create(
            user=user,
            paid_course=course,
            paid_lesson=lesson,
            payment_amount=payment_amount,
            payment_method=payment_method
        )

        self.stdout.write(self.style.SUCCESS('Данные успешно добавлены в модель Payment'))