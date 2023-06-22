from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from users.models import CustomUser
from users.api.serializers import UserProfileSerializer


class UserDataViewSet(viewsets.ViewSet):
    """ Вьюсет данных о пользователе """

    permission_classes = []

    @swagger_auto_schema(
        responses={
            200: openapi.Response(
                'Данные о пользователе',
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
        operation_summary='Получить данные о пользователе по его id.',
    )
    @action(methods=['get'], detail=False)
    def me(self, request, uid):
        """ Получает данные о пользователе по id """
        try:
            user = CustomUser.objects.get(id=uid)
        except CustomUser.DoesNotExist:
            return Response(
                {
                    'description': f'Пользователь не найден!'
                },
                status=status.HTTP_404_NOT_FOUND
            )
        return Response(UserProfileSerializer(user).data, status=status.HTTP_200_OK)
