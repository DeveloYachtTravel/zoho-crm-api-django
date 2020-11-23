from django.db import models


class AuthToken(models.Model):
    useridentifier = models.EmailField(primary_key=True)
    accesstoken = models.CharField(max_length=100)
    refreshtoken = models.CharField(max_length=100)
    expirytime = models.BigIntegerField()