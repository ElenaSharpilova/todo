# Generated by Django 3.1.3 on 2021-01-22 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210121_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookshop',
            name='is_favorites',
            field=models.BooleanField(default=False),
        ),
    ]
