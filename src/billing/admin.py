from django.contrib import admin

from billing.models import TransactionModel


@admin.register(TransactionModel)
class TransactionModelAdmin(admin.ModelAdmin):
    """ TransactionModel admin """

    list_display = (
        'user', 'amount', 'date_created',
    )
    readonly_fields = ('user', 'amount', 'date_created')
