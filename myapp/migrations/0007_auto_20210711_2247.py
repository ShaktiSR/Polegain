# Generated by Django 3.1.7 on 2021-07-11 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_ulimiter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ulimiter',
            name='ulimit',
            field=models.IntegerField(default=0),
        ),
    ]