from rest_framework import serializers

from .models import (EducationQualification, Post, Slider,
                     Student_Registration, User)


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class sliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = "__all__"


class Student_info(serializers.ModelSerializer):
    class Meta:
        model = Student_Registration
        fields = "__all__"


class Education_info(serializers.ModelSerializer):
    class Meta:
        model = EducationQualification
        fields = "__all__"
