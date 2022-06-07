from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .filters import CategoryFilter, ToDoFilter
from .mixins import MultipleObjectCreate
from .models import Category, ToDo
from .pagination import BasicPagination
from .permissions import IsOwnerPermission
from .serializers import (
    CategorySerializer,
    MultipleToDoSerializer,
    ToDoSerializer,
    UserSerializer,
)

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
    queryset = ToDo.objects.all().order_by("created_at")
    serializer_class = ToDoSerializer
    permission_classes = (IsOwnerPermission,)
    filter_backends = [DjangoFilterBackend]
    filterset_class = ToDoFilter
    pagination_class = BasicPagination

    def get_queryset(self):
        return self.queryset.filter(created_by=self.request.user)


class MultipleToDoDeleteView(APIView):
    serializer_class = MultipleToDoSerializer
    permission_classes = (IsOwnerPermission,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            todo_id = serializer.validated_data["todo_id"]
            todos = ToDo.objects.filter(id__in=todo_id).delete()
            return Response(
                {"success": f"{todos[0]} tasks were deleted."},
                status=status.HTTP_200_OK,
            )
