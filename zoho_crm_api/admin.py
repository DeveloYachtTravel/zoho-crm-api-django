from django.contrib import admin

from .django_models import AuthToken


@admin.register(AuthToken)
class AuthTokenAdmin(admin.ModelAdmin):
    list_display = ('useridentifier','accesstoken','expirytime')