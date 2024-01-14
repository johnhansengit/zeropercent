# Generated by Django 5.0.1 on 2024-01-14 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0020_recipe_uploaded_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='img',
            field=models.URLField(blank=True, max_length=1000, verbose_name='or paste photo url'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='uploaded_img',
            field=models.ImageField(blank=True, null=True, upload_to='recipe_photos/', verbose_name='feature photo'),
        ),
    ]
