# Generated by Django 3.2.4 on 2021-06-21 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('slack_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CountDown',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('happening', models.CharField(max_length=1000)),
                ('description', models.TextField(max_length=20000)),
                ('status', models.CharField(choices=[('0', 'new'), ('1', 'running'), ('2', 'done')], default='0', max_length=20)),
                ('start', models.DateTimeField(blank=True, default='2021-06-21T13:01:20.258288', null=True)),
                ('end', models.DateTimeField(blank=True, null=True)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_countdowns', to='app.channel')),
            ],
        ),
    ]
