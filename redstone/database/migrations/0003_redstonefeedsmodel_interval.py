# Generated by Django 2.0.7 on 2018-07-31 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_redstonespidermodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='redstonefeedsmodel',
            name='interval',
            field=models.IntegerField(default=30),
        ),
    ]
