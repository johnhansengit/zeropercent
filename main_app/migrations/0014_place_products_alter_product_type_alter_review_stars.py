# Generated by Django 5.0.1 on 2024-01-12 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_place_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='products',
            field=models.ManyToManyField(to='main_app.product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.IntegerField(choices=[(1, '0% beer'), (1, '0% cider'), (1, '0% wine'), (1, '0% champagne'), (1, '0% gin'), (1, '0% rum'), (1, '0% vodka'), (1, '0% tequila'), (1, '0% whiskey')], default=1),
        ),
        migrations.AlterField(
            model_name='review',
            name='stars',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=5),
        ),
    ]
