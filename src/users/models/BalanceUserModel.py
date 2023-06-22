from django.db import models


class BalanceUser(models.Model):
    """ Баланс пользователя """

    user = models.ForeignKey(
        'users.CustomUser',
        verbose_name='Владелец баланса',
        related_name='%(class)ss',
        null=True,
        on_delete=models.SET_NULL,
    )
    balance = models.IntegerField('Баланс', default=0)

    class Meta:
        verbose_name = 'Balance info'
        verbose_name_plural = 'Balance info'

    def __str__(self):
        """ Возвращаем баланс """
        return str(self.balance)
