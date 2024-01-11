from django import forms
from .models import Review, Recipe, Category

class ReviewForm(forms.ModelForm):
  class Meta:
    model = Review
    fields = ['reviewer', 'stars', 'review']

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'category', 'ingredients', 'instructions', 'difficulty', 'prep', 'img']

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
    new_category = forms.CharField(
       required=False, 
       max_length=100,
       label='or add a new category')
