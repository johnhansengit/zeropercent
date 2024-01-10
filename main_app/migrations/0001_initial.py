# Generated by Django 5.0.1 on 2024-01-10 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('ingredients', models.TextField(max_length=500)),
                ('instructions', models.TextField(blank=True, max_length=1000)),
                ('difficulty', models.IntegerField()),
                ('prep', models.IntegerField(blank=True, null=True)),
                ('img', models.URLField(blank=True)),
            ],
        ),
    ]