from rest_framework import serializers

from users.models import CustomUser


class UserProfileSerializer(serializers.ModelSerializer):
    """ Сериализация модели пользователя """

    balance = serializers.SerializerMethodField()

    def get_balance(self, instance):
        """ форматировать баланс """
        return int(instance.balance.balance)

    class Meta:
        fields = [
            'id',
            'login',
            'email',
            'balance',
        ]
        model = CustomUser
