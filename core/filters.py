import django_filters
from .models import ToDo, Category


class CategoryFilter(django_filters.FilterSet):
    class Meta:
        model = Category
        fields = {
            "id": ["exact"],
            "name": ["icontains"],
            "created_by": ["exact"],
            "created_at": ["date__lte", "date__gte"],
        }


class ToDoFilter(django_filters.FilterSet):
    class Meta:
        model = ToDo
        fields = {
            "category": ["exact"],
            "id": ["exact"],
            "title": ["icontains"],
            "created_at": ["date__lte ", "date__gte"],
            "deadline": ["date__lte", "date__gte"],
        }

