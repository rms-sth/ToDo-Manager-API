import django_filters
from .models import ToDo, Category


class CategoryFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = Category
        fields = {
            "id": ["exact"],
            "created_by": ["exact"],
            "created_at": ["date__lte", "date__gte"],
        }


class ToDoFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name="title", lookup_expr="icontains")

    class Meta:
        model = ToDo
        fields = {
            "category": ["exact"],
            "id": ["exact"],
            "created_at": ["date__lte", "date__gte"],
            "deadline": ["date__lte", "date__gte"],
        }

