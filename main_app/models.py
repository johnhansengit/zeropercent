from django.db import models
from django.urls import reverse

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    ingredients = models.TextField(max_length=1000)
    instructions = models.TextField(blank=True)
    difficulty = models.IntegerField()
    prep = models.IntegerField(null=True, blank=True)
    img = models.URLField(max_length=1000, blank=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'drink_id': self.id})