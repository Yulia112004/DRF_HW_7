from rest_framework import serializers

from course.models import Course, Subscription
from lesson.models import Lesson
from lesson.serializers import LessonSerializer


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, source='lesson')
    is_subscribed = serializers.SerializerMethodField()

    def get_lessons_count(self, course):
        return Lesson.objects.filter(course=course).count()

    def get_lessons(self, course):
        return [lesson.title for lesson in course.lesson_set.all()]

    def get_is_subscribed(self, course):
        return Subscription.objects.filter(course=course, user=self.context['request'].user).exists()

    class Meta:
        model = Course
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'