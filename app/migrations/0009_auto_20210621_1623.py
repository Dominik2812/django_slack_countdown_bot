# Generated by Django 3.2.4 on 2021-06-21 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_countdown_c_start'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='countdown',
            name='c_description',
        ),
        migrations.RemoveField(
            model_name='countdown',
            name='c_status',
        ),
        migrations.AlterField(
            model_name='channel',
            name='slack_id',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='countdown',
            name='c_start',
            field=models.DateTimeField(blank=True, default='2021-06-21T14:23:22.813326', null=True),
        ),
    ]
