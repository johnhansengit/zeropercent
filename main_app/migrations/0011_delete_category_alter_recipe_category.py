# Generated by Django 5.0.1 on 2024-01-11 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_alter_recipe_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='category',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
