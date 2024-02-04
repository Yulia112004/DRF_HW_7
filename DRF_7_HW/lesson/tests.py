from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.
from course.models import Course
from lesson.models import Lesson
from users.models import User


class LessonTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='test_user@test.ru',
                                        phone='test_phone',
                                        is_staff=True,
                                        is_superuser=True,
                                        is_active=True)

        self.user.set_password('qwerty')
        self.user.save()


        self.course = Course.objects.create(title='Тестовый курс',
                                            description='Описание тестового курса',
                                            owner=self.user)


        self.lesson = Lesson.objects.create(title='Урок 25.2',
                                            description='Описание урока 25.2',
                                            url='https://www.youtube.com/',
                                            owner=self.user,
                                            course=self.course)


        response = self.client.post('/users/token/', data={'email': self.user.email, 'password': 'qwerty'})

        self.access_token = response.data.get('access')

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

    def test_create_lesson(self):
        data = {
            'title': 'Урок 25.2 другой',
            "description": "Описание урока 25.2 другое",
            'course': self.course.pk,
            'url': 'https://www.youtube.com/',
        }

        response = self.client.post(reverse('lesson:lesson_create'), data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_list_lessons(self):

        response = self.client.get(reverse('lesson:lessons'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.json(),
                         [{'id': self.lesson.pk,
                           'title': self.lesson.title,
                           'description': self.lesson.description,
                           'preview': None,
                           'url': self.lesson.url,
                           'course': self.course.pk,
                           'owner': self.user.pk}]
                         )

    def test_update_lessons(self):
        data = {
            'title': 'Урок 25.2 измененный',
            "description": "Описание урока 25.2 измененное",
            'preview': '',
            'url': 'https://www.youtube.com/',
            'course': self.course.pk,
            'owner': self.user.pk
        }

        response = self.client.put(reverse('lesson:lesson_update', args=[self.lesson.pk]), data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.json(),
                         {'id': self.lesson.pk,
                          'title': "Урок 25.2 измененный",
                          'description': 'Описание урока 25.2 измененное',
                          'preview': None,
                          'url': self.lesson.url,
                          'course': self.course.pk,
                          'owner': self.user.pk}
                         )

    def test_get_lessons_by_id(self):
        response = self.client.get(reverse('lesson:lesson', args=[self.lesson.pk]))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.json(),
                         {'id': self.lesson.pk,
                          'title': self.lesson.title,
                          'description': self.lesson.description,
                          'preview': None,
                          'url': self.lesson.url,
                          'course': self.course.pk,
                          'owner': self.user.pk}
                         )

    def test_destroy_lessons(self):
        response = self.client.delete(reverse('lesson:lesson_delete', args=[self.lesson.pk]))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertEqual(Lesson.objects.all().count(), 0)