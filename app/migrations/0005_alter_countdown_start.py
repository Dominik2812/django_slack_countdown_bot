# Generated by Django 3.2.4 on 2021-06-21 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_countdown_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countdown',
            name='start',
            field=models.DateTimeField(blank=True, default='2021-06-21T13:07:03.748124', null=True),
        ),
    ]
