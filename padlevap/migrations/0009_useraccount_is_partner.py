# Generated by Django 5.1.6 on 2025-07-07 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('padlevap', '0008_remove_test_image_url_test_image_en_alter_test_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='is_partner',
            field=models.BooleanField(default=False),
        ),
    ]
