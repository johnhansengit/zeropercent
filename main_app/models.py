from django.db import models
from django.urls import reverse
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    DIFFICULTIES = (
        (1, 'so easy!'),
        (2, 'easy enough'),
        (3, 'takes a bit of work'),
        (4, 'takes real patience!'),
    )
    
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    ingredients = models.TextField(max_length=1000)
    instructions = models.TextField(blank=True)
    difficulty = models.IntegerField(choices=DIFFICULTIES, default=DIFFICULTIES[0][0])
    prep = models.IntegerField('prep time (in minutes)', null=True, blank=True)
    img = models.URLField('feature photo (url)', max_length=1000, blank=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'recipe_id': self.id})
    

class Review(models.Model):
    STARPICKER = (
        (1, 1), 
        (2, 2), 
        (3, 3), 
        (4, 4), 
        (5, 5)
    )

    reviewer = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now)
    stars = models.IntegerField(choices=STARPICKER, default=STARPICKER[4][0])
    review = models.TextField(max_length=1000, blank=True)

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.reviewer} left a {self.get_stars_display()}-star review on {self.date}"
    
    class Meta:
        ordering = ['-date']

class Product(models.Model):
    PRODUCTTYPES = (
        (1, '0% beer'),
        (1, '0% cider'),
        (1, '0% wine'),
        (1, '0% champagne'),
        (1, '0% gin'),
        (1, '0% rum'),
        (1, '0% vodka'),
        (1, '0% tequila'),
        (1, '0% whiskey'),
    )
    name = models.CharField(max_length=100)
    type = models.IntegerField(choices=PRODUCTTYPES, default=PRODUCTTYPES[0][0])

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'product_id': self.id})
    
    class Meta:
        ordering = ['name']

class Place(models.Model):
    name = models.CharField(max_length=100)
    open_hours = models.CharField('open hours (.e.g. M-F, 4p-2a)', max_length=100, blank=True)
    google_maps = models.URLField('Google Maps (url)', max_length=1000, blank=True)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'place_id': self.id})
