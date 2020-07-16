from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .mixins import MultipleObjectCreate
from .models import Category, ToDo
from .permissions import IsOwnerPermission
from .serializers import CategorySerializer, ToDoSerializer, UserSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import CategoryFilter, ToDoFilter
from .pagination import BasicPagination

User = get_user_model()


class UserViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == "list" or self.action == "retrieve":
            return [
                IsAuthenticated(),
            ]
        return super().get_permissions()

    def get_queryset(self):
        return User.objects.all().exclude(id=self.request.user.id).order_by("username")


class CategoryViewSet(MultipleObjectCreate, ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsOwnerPermission,)
    filter_backends = [DjangoFilterBackend]
    filterset_class = CategoryFilter
    pagination_class = BasicPagination

    def get_queryset(self):
        return Category.objects.filter(created_by=self.request.user)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context


class ToDoViewSet(MultipleObjectCreate, ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = (IsOwnerPermission,)
    filter_backends = [DjangoFilterBackend]
    filterset_class = ToDoFilter
    pagination_class = BasicPagination

    def get_queryset(self):
        return ToDo.objects.filter(created_by=self.request.user)
