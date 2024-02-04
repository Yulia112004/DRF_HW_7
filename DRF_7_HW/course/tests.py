from django.urls import reverse
from rest_framework import status

# Create your tests here.
from course.models import Subscription
from lesson.tests import LessonTestCase


class SubscriptionTestCase(LessonTestCase):
    def test_subscribe_unsubscribe_course(self):
        data = {
            'user': self.user.pk,
            # 'course': self.course.pk,
        }

        response = self.client.post(reverse('course:subscribe', args=[self.course.pk]), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Subscription.objects.filter(user=self.user, course=self.course).exists(), True)
        response = self.client.delete(reverse('course:unsubscribe', args=[self.course.pk]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Subscription.objects.filter(user=self.user, course=self.course).exists(), False)