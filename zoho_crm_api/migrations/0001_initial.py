# Generated by Django 3.0 on 2020-11-23 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthToken',
            fields=[
                ('useridentifier',models.EmailField(primary_key=True)),
                ('accesstoken', models.CharField(max_length=100)),
                ('refreshtoken', models.CharField(max_length=100)),
                ('expirytime', models.BigIntegerField())
            ],
        ),
    ]
