from django.shortcuts import render, redirect
from django.db.models import Avg
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Recipe, Review, Category
from .forms import ReviewForm, RecipeForm

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def drinks_index(request):
  drinks = Recipe.objects.all()

  for drink in drinks:
    reviews = Review.objects.filter(recipe=drink)
    average_rating = reviews.aggregate(Avg('stars'))['stars__avg']
    drink.average_rating = round(average_rating, 1) if average_rating is not None else '(no ratings)'

  return render(request, 'drinks/index.html', {
    'drinks': drinks
})


def drinks_detail(request, drink_id):
  drink = Recipe.objects.get(id=drink_id)
  review_form = ReviewForm()
  return render(request, 'drinks/detail.html', {
    'drink': drink,
    'review_form': review_form
  })

def add_review(request, drink_id):
  form = ReviewForm(request.POST)
  if form.is_valid():
    new_review = form.save(commit=False)
    new_review.recipe_id = drink_id
    new_review.save()
  return redirect('detail', drink_id=drink_id)

class DrinkCreate(CreateView):
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
      return super(DrinkCreate, self).form_valid(form)

class DrinkUpdate(UpdateView):
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
      return super(DrinkUpdate, self).form_valid(form)

class DrinkDelete(DeleteView):
  model = Recipe
  success_url = '/drinks'
