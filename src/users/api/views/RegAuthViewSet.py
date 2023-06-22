from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import login, authenticate, logout

from users.models import CustomUser
from users.api.serializers import UserProfileSerializer


class RegAuthViewSet(viewsets.ViewSet):
    """ Вьюсет регистрации/авторизации пользователя """

    permission_classes = []

    @swagger_auto_schema(
        responses={
            200: openapi.Response(
                'Регистрация пользователя.',
                examples={
                    'application/json': {
                        'id': 'integer',
                        'email': 'string',
                        'name': 'string',
                        'balance': 'integer',
                    },
                },
            ),
        },
        operation_summary='Регистрация пользователя.',
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'name': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description='Имя пользователя',
                ),
                'email': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description='Email',
                ),
                'pwd': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description='Пароль',
                ),
            },
        ),
    )
    @action(methods=['post'], detail=False)
    def registration(self, request):
        """Регистрация пользователя."""
        email = request.data.get('email')
        name = request.data.get('name')
        pwd = request.data.get('pwd')

        if CustomUser.objects.filter(email=email).exists():
            return Response(
                {
                    'description': f'Аккаунт с почтой {email} уже существует!',
                },
                status=status.HTTP_302_FOUND
            )
        user = CustomUser.objects.create_user(email, name, pwd)
        login(request, user)
        return Response(UserProfileSerializer(user).data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={
            200: openapi.Response(
                'Регистрация пользователя.',
                examples={
                    'application/json': {
                        'id': 'integer',
                        'email': 'string',
                        'name': 'string',
                        'balance': 'integer',
                    },
                },
            ),
        },
        operation_summary='Авторизация пользователя.',
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'email': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description='Email',
                ),
                'pwd': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description='Пароль',
                ),
            },
        ),
    )
    @action(methods=['post'], detail=False)
    def authorization(self, request):
        """Авторизация пользователя."""
        email = request.data.get('email')
        pwd = request.data.get('pwd')

        user = authenticate(request, email=email, password=pwd)
        if not user:
            return Response(
                {
                    'description': f'Пользователь с адресом {email} не зарегистрирован!'
                },
                status=status.HTTP_204_NO_CONTENT
            )
        login(request, user)
        return Response(UserProfileSerializer(user).data, status=status.HTTP_200_OK)
