# Generated by Django 3.2.4 on 2021-06-23 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20210622_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='countdown',
            name='c_status',
            field=models.CharField(choices=[('upcoming', 'upcoming'), ('done', 'done'), ('deleting', 'deleting')], default='0', max_length=20),
        ),
        migrations.AlterField(
            model_name='countdown',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
