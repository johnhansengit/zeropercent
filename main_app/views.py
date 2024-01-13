from django.shortcuts import render, redirect
from django.db.models import Avg
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Recipe, Review, Category, Product, Place
from .forms import ReviewForm, RecipeForm
import os
from dotenv import load_dotenv

load_dotenv()  

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def recipes_index(request):
  recipes = Recipe.objects.all()

  for recipe in recipes:
    reviews = Review.objects.filter(recipe=recipe)
    average_rating = reviews.aggregate(Avg('stars'))['stars__avg']
    
    if average_rating is not None:
      recipe.average_rating = round(int(average_rating))
      recipe.stars_filled = range(recipe.average_rating)
      recipe.stars_empty = range(5 - recipe.average_rating)
    else:
      recipe.average_rating = '(no ratings)'
      recipe.stars_filled = []
      recipe.stars_empty = []

  return render(request, 'recipes/index.html', {
    'recipes': recipes
})


def recipes_detail(request, recipe_id):
  recipe = Recipe.objects.get(id=recipe_id)
  review_form = ReviewForm()

  reviews = Review.objects.filter(recipe=recipe)
  average_rating = reviews.aggregate(Avg('stars'))['stars__avg']
  if average_rating is not None:
    recipe.average_rating = round(int(average_rating))
    recipe.stars_filled = range(recipe.average_rating)
    recipe.stars_empty = range(5 - recipe.average_rating)
  else:
    recipe.average_rating = '(no ratings)'
    recipe.stars_filled = []
    recipe.stars_empty = []
  
  for review in reviews:
    recipe.stars_range = range(review.stars)
  
  return render(request, 'recipes/detail.html', {
    'recipe': recipe,
    'review_form': review_form
  })

def add_review(request, recipe_id):
  form = ReviewForm(request.POST)
  if form.is_valid():
    new_review = form.save(commit=False)
    new_review.recipe_id = recipe_id
    new_review.save()
  return redirect('detail', recipe_id=recipe_id)

class RecipeCreate(CreateView):
  model = Recipe
  form_class = RecipeForm

  def form_valid(self, form):
      new_category_name = form.cleaned_data['new_category']
      if new_category_name:
          category, created = Category.objects.get_or_create(name=new_category_name)
          self.object = form.save(commit=False)
          self.object.category = category
          self.object.save()
      else:
          self.object = form.save()
      return super(RecipeCreate, self).form_valid(form)

class RecipeUpdate(UpdateView):
  model = Recipe
  form_class = RecipeForm

  def form_valid(self, form):
      new_category_name = form.cleaned_data.get('new_category', None)
      if new_category_name:
          category, created = Category.objects.get_or_create(name=new_category_name)
          self.object = form.save(commit=False)
          self.object.category = category
          self.object.save()
      else:
          self.object = form.save()
      return super(RecipeUpdate, self).form_valid(form)

class RecipeDelete(DeleteView):
  model = Recipe
  success_url = '/recipes'

class ProductList(ListView):
  model = Product

class ProductDetail(DetailView):
  model = Product

class ProductCreate(CreateView):
  model = Product
  fields = '__all__'

class ProductUpdate(UpdateView):
  model = Product
  fields = '__all__'

class ProductDelete(DeleteView):
  model = Product
  success_url = '/products'

class PlaceList(ListView):
  model = Place

def places_detail(request, place_id):
  place = Place.objects.get(id=place_id)
  
  id_list = place.products.all().values_list('id')
  products_place_doesnt_have = Product.objects.exclude(id__in=id_list)

  google_maps_api_key = os.environ.get('GOOGLE_MAPS_API_KEY')
  
  return render(request, 'main_app/place_detail.html', {
    'place': place,
    'products': products_place_doesnt_have,
    'maps_api': google_maps_api_key,
  })

class PlaceCreate(CreateView):
  model = Place
  fields = ['name', 'open_hours', 'address']

class PlaceUpdate(UpdateView):
  model = Place
  fields = ['name', 'open_hours', 'address']

class PlaceDelete(DeleteView):
  model = Place
  success_url = '/places'

def assoc_product(request, place_id, product_id):
  Place.objects.get(id=place_id).products.add(product_id)
  return redirect('places_detail', place_id=place_id)

def disassoc_product(request, place_id, product_id):
  Place.objects.get(id=place_id).products.remove(product_id)
  return redirect('places_detail', place_id=place_id)