# Generated by Django 5.0.1 on 2024-01-14 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0023_alter_recipe_img'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ['name']},
        ),
    ]
