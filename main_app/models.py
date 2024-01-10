from django.db import models

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    ingredients = models.TextField(max_length=500)
    instructions = models.TextField(max_length=1000, blank=True)
    difficulty = models.IntegerField()
    prep = models.IntegerField(null=True, blank=True)
    img = models.URLField(blank=True)