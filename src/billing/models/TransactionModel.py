from django.db import models

from users.models.BalanceUserModel import BalanceUser


class TransactionModel(models.Model):
    """ Модель транзакций """

    user = models.ForeignKey(
        'users.CustomUser',
        verbose_name='Владелец транзакции',
        related_name='%(class)ss',
        null=True,
        on_delete=models.SET_NULL,
    )
    amount = models.IntegerField('Сумма транзакции')
    date_created = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Transaction info'
        verbose_name_plural = 'Transaction info'

    def save(self, *args, **kwargs):
        """ Хук метода save """
        if self.amount and self.user:
            obj, create = BalanceUser.objects.get_or_create(user=self.user)
            if create:
                create.balance = self.amount
                create.save()
                self.user.balance = create
            else:
                obj.balance = self.amount
                obj.save()
                self.user.balance = obj
            self.user.save()
        super(TransactionModel, self).save(*args, **kwargs)

    def __str__(self):
        """ Возвращаем id транзакции и email юзера """
        return f'{self.id} | {self.user.email}'
