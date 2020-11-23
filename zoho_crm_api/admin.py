from django.contrib import admin

from .database.models import AuthToken


@admin.register(AuthToken)
class AuthTokenAdmin(admin.ModelAdmin):
    list_display = ('useridentifier','accesstoken','expirytime')