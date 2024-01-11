from django.db import models
from django.urls import reverse
from django.utils import timezone

class Recipe(models.Model):
    DIFFICULTIES = (
        (1, 'so easy!'),
        (2, 'easy enough'),
        (3, 'takes a bit of work'),
        (4, 'takes real patience!'),
    )
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    ingredients = models.TextField(max_length=1000)
    instructions = models.TextField(blank=True)
    difficulty = models.IntegerField(choices=DIFFICULTIES, default=DIFFICULTIES[0][0])
    prep = models.IntegerField('prep time (in minutes)', null=True, blank=True)
    img = models.URLField('feature photo (url)', max_length=1000, blank=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'drink_id': self.id})

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
    stars = models.IntegerField(choices=STARPICKER, default=STARPICKER[0][0])
    review = models.TextField(max_length=1000, blank=True)

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.reviewer} left a {self.get_stars_display()}-star review on {self.date}"
    
    class Meta:
        ordering = ['-date']
