from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Recipe

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def drinks_index(request):
  drinks = Recipe.objects.all()
  return render(request, 'drinks/index.html', {
    'drinks': drinks
  })

def drinks_detail(request, drink_id):
  drink = Recipe.objects.get(id=drink_id)
  return render(request, 'drinks/detail.html', {
    'drink': drink
  })

class DrinkCreate(CreateView):
  model = Recipe
  fields = '__all__'

class DrinkUpdate(UpdateView):
  model = Recipe
  fields = '__all__'

class DrinkDelete(DeleteView):
  model = Recipe
  success_url = '/drinks'
