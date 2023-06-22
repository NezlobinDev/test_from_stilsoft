from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from billing.models import TransactionModel
from billing.api.serializers import TransactionSerializer
from users.models import CustomUser


class TransactionListViewSet(viewsets.ViewSet):
    """ Вьюсет транзакций """

    permission_classes = []

    @swagger_auto_schema(
        responses={
            200: openapi.Response(
                'Топ 10 транзакций',
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
        operation_summary='Топ транзакций.',
    )
    @action(methods=['get'], detail=False)
    def top_transactions(self, request):
        """ Выводит топ 10 транзакций """
        transaction_queryset = TransactionModel.objects.filter().order_by('-amount')[:10]
        if not transaction_queryset:
            return Response(
                {
                    'description': 'Транзакций не найдено!',
                },
                status=status.HTTP_404_NOT_FOUND
            )
        return Response(
            TransactionSerializer(transaction_queryset, many=True).data,
            status=status.HTTP_200_OK,
        )

    @swagger_auto_schema(
        responses={
            200: openapi.Response(
                'Транзакции пользователя',
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
        operation_summary='Транзакции пользователя.',
    )
    @action(methods=['get'], detail=True)
    def user_transactions(self, request, pk):
        """ Выводит список транзакций юзера

        В id передается id пользователя по которому хотим получить информацию.
        """
        try:
            user = CustomUser.objects.get(id=pk)
        except CustomUser.DoesNotExist:
            return Response(
                {
                    'description': f'Пользователь с id: {pk} не найден!'
                },
                status=status.HTTP_404_NOT_FOUND,
            )
        transaction_queryset = TransactionModel.objects.filter(user=user).order_by('-id')
        if not transaction_queryset:
            return Response(
                {
                    'description': f'Пользователь {pk} не совершал транзакций!',
                },
                status=status.HTTP_404_NOT_FOUND
            )
        return Response(
            TransactionSerializer(transaction_queryset, many=True).data,
            status=status.HTTP_200_OK,
        )
