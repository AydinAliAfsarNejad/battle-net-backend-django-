# Generated by Django 5.2 on 2025-05-31 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_games_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='games',
            old_name='Price',
            new_name='price',
        ),
    ]
