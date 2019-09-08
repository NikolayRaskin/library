from django.contrib.auth.models import User
from base.models import User_Profile
from user_profile.models import Book
from rest_framework import serializers


class User_ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Profile
        fields = '__all__'
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'