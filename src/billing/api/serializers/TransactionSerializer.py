from rest_framework import serializers

from billing.models import TransactionModel
from users.api.serializers import UserProfileSerializer


class TransactionSerializer(serializers.ModelSerializer):
    """ Сериализатор модели Transaction """

    user = UserProfileSerializer(read_only=True)
    date_create = serializers.SerializerMethodField()

    def get_date_create(self, instance):
        """ Форматирование даты и времени """
        return instance.date_created.strftime('%d.%m.%Y %H:%M')

    class Meta:
        fields = [
            'id',
            'amount',
            'user',
            'date_create',
        ]
        model = TransactionModel
