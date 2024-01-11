# Generated by Django 5.0.1 on 2024-01-11 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_recipe_difficulty_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='difficulty',
            field=models.IntegerField(choices=[(1, 'so easy!'), (2, 'easy enough'), (3, 'takes a bit of work'), (4, 'takes real patience!')], default=1),
        ),
    ]