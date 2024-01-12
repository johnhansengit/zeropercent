from django.shortcuts import render, redirect
from django.db.models import Avg
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Recipe, Review, Category
from .forms import ReviewForm, RecipeForm

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def recipes_index(request):
  recipes = Recipe.objects.all()

  for recipe in recipes:
    reviews = Review.objects.filter(recipe=recipe)
    average_rating = reviews.aggregate(Avg('stars'))['stars__avg']
    recipe.average_rating = round(average_rating, 1) if average_rating is not None else '(no ratings)'

  return render(request, 'recipes/index.html', {
    'recipes': recipes
})


def recipes_detail(request, recipe_id):
  recipe = Recipe.objects.get(id=recipe_id)
  review_form = ReviewForm()
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
  fields = '__all__'

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
