from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from users.models import User
from users.permissions import IsOwner
from users.serializers import UserSerializer
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    serializers_class = UserSerializer
    queryset = get_user_model().objects.all()
    perms_methods = {
        'create': [AllowAny],
        'list': [IsAuthenticated],
        'update': [IsAuthenticated, IsOwner | IsAdminUser],
        'partial_update': [IsAuthenticated, IsOwner | IsAdminUser],
        'destroy': [IsAuthenticated, IsOwner | IsAdminUser],
    }

    def permissions(self):
        self.permission_classes = self.perms_methods.get(self.actions, self.permission_classes)
        return [permission() for permission in self.permission_classes]

    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        password = request.data.get('password')
        user = User.objects.get(email=serializer.data.get('email'))
        user.set_password(password)
        user.save()
        return Response(serializer.data, status=201, headers=headers)

    def retrieve(self, request, *args, **kwargs):
        if self.request.user == self.get_object() or self.request.user.is_superuser:
            serializer_class = UserSerializer
        else:
            serializer_class = UserSerializer
        serializer = serializer_class(self.get_object())
        serializer_data = serializer.data

        return Response(serializer_data)
