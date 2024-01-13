from django.contrib import admin
from .models import Recipe, Review, Category, Product, Place

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Review)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Place)
