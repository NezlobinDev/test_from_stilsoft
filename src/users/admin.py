from django.contrib import admin

from users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    """ CustomUser admin """

    list_display = (
        'login', 'email', 'date_created',
    )
    readonly_fields = ('balance',)
