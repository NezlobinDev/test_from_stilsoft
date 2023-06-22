from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from billing.models import TransactionModel
from billing.api.serializers import TransactionSerializer
from users.models import CustomUser, BalanceUser


class TransactionViewSet(viewsets.ViewSet):
    """ Вьюсет транзакций """

    permission_classes = []

    @swagger_auto_schema(
        responses={
            200: openapi.Response(
                'Создание транзакции',
                examples={
                    'application/json': {
                        'id': 'integer',
                        'user': {
                            'id': 'integer',
                            'email': 'string',
                            'name': 'string',
                            'balance': 'integer',
                        },
                        'amount': 'integer',
                        'date_create': 'dd.mm.yyyy hh:mm',
                    },
                },
            ),
        },
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'uid': openapi.Schema(
                    type=openapi.TYPE_INTEGER,
                    description='id пользователя',
                ),
                'amount': openapi.Schema(
                    type=openapi.TYPE_INTEGER,
                    description='Сумма транзакции',
                ),
            },
        ),
        operation_summary='Создать транзакцию.',
    )
    def create(self, request):
        """ Создает транзакцию по id юзера """
        uid = request.data.get('uid', None)
        amount = request.data.get('amount', None)

        if not uid:
            return Response(
                {
                    'description': 'Ошибка валидации! Поле `uid` обязательно!',
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        if not amount:
            return Response(
                {
                    'description': 'Ошибка валидации! Поле `uid` обязательно!',
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            user = CustomUser.objects.get(id=uid)
        except CustomUser.DoesNotExist:
            return Response(
                {
                    'description': 'Пользователь не найден!'
                },
                status=status.HTTP_404_NOT_FOUND
            )
        transaction = TransactionModel.objects.create(
            user=user,
            amount=int(amount),
        )

        return Response(
            TransactionSerializer(transaction).data,
            status=status.HTTP_200_OK,
        )

    @swagger_auto_schema(
        responses={
            200: openapi.Response(
                'Информация о транзакции',
                examples={
                    'application/json': {
                        'id': 'integer',
                        'user': {
                            'id': 'integer',
                            'email': 'string',
                            'name': 'string',
                            'balance': 'integer',
                        },
                        'amount': 'integer',
                        'date_create': 'dd.mm.yyyy hh:mm',
                    },
                },
            ),
        },
        operation_summary='Информация о транзакции юзера.',
    )
    @action(methods=['get'], detail=True)
    def info(self, request, pk):
        """ Получает информацию о транзакции """
        try:
            transaction = TransactionModel.objects.get(id=pk)
        except TransactionModel.DoesNotExist:
            return Response(
                {
                    'description': 'Транзакция не найдена!'
                },
                status=status.HTTP_404_NOT_FOUND
            )
        return Response(
            TransactionSerializer(transaction).data,
            status=status.HTTP_200_OK,
        )

    @swagger_auto_schema(
        responses={
            200: openapi.Response(
                'Редактирование транзакции',
                examples={
                    'application/json': {
                        'id': 'integer',
                        'user': {
                            'id': 'integer',
                            'email': 'string',
                            'name': 'string',
                            'balance': 'integer',
                        },
                        'amount': 'integer',
                        'date_create': 'dd.mm.yyyy hh:mm',
                    },
                },
            ),
        },
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'amount': openapi.Schema(
                    type=openapi.TYPE_INTEGER,
                    description='Сумма транзакции',
                ),
            },
        ),
        operation_summary='Информация о транзакции юзера.',
    )
    @action(methods=['post'], detail=True)
    def edit(self, request, pk):
        """ Редактирует транзакцию по id"""
        amount = request.data.get('amount', None)
        if not amount:
            return Response(
                {
                    'description': 'Ошибка валидации! Поле `amount` обязательно!',
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            transaction = TransactionModel.objects.get(id=pk)
        except TransactionModel.DoesNotExist:
            return Response(
                {
                    'description': 'Транзакция не найдена!'
                },
                status=status.HTTP_404_NOT_FOUND
            )
        if int(amount) < 0:
            return Response(
                {
                    'description': 'Ошибка валидации! Поле `amount` не может быть меньше 0!',
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        transaction.amount = int(amount)
        transaction.save()
        return Response(
            TransactionSerializer(transaction).data,
            status=status.HTTP_200_OK,
        )

    @action(methods=['post'], detail=True)
    def delete(self, request, pk):
        """ Удаляет транзакцию """
        try:
            transaction = TransactionModel.objects.get(id=pk)
        except TransactionModel.DoesNotExist:
            return Response(
                {
                    'description': 'Транзакция не найдена!'
                },
                status=status.HTTP_404_NOT_FOUND
            )
        transaction.delete()
        return Response({}, status=status.HTTP_200_OK)
