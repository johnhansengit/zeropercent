# Generated by Django 5.0.1 on 2024-01-14 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0024_alter_recipe_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='place',
            options={'ordering': ['name']},
        ),
    ]