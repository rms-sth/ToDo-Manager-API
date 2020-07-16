from django.contrib.auth import get_user_model
from rest_framework import serializers

from core.models import Category, ToDo

from .models import Category, ToDo

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["password"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "created_at", "created_by"]
        extra_kwargs = {
            "created_by": {"read_only": True},
        }


class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ["id", "title", "category", "created_at", "created_by", "deadline"]
        extra_kwargs = {
            "created_by": {"read_only": True},
        }
