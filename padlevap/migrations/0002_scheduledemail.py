# Generated by Django 5.1.6 on 2025-04-19 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('padlevap', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduledEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('welcome_sent', models.BooleanField(default=False)),
                ('day1_sent', models.BooleanField(default=False)),
                ('day2_sent', models.BooleanField(default=False)),
                ('day3_sent', models.BooleanField(default=False)),
                ('is_completed', models.BooleanField(default=False)),
            ],
        ),
    ]
