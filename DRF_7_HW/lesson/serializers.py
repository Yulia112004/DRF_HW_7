from rest_framework import serializers

from lesson.models import Lesson
from lesson.validators import LinkToVideoValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [LinkToVideoValidator('url')]