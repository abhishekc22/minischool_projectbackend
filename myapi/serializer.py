from rest_framework import serializers
from .models import *


class Studentserializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class Teacherserializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"


class Subjectserializerall(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"
        depth = 2


class Subjectserializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"
