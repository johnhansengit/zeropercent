# Generated by Django 5.0.1 on 2024-01-12 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_category_alter_recipe_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('open_hours', models.CharField(blank=True, max_length=100, verbose_name='open hours (.e.g. M-F, 4p-2a)')),
                ('google_maps', models.URLField(blank=True, max_length=1000, verbose_name='Google Maps (url)')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.IntegerField(choices=[(1, '0% beer'), (1, '0% wine'), (1, '0% gin'), (1, '0% rum'), (1, '0% vodka'), (1, '0% tequila'), (1, '0% whiskey')], default=1)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
