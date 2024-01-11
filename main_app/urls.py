from django.urls import path
from . import views
	
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('drinks/', views.drinks_index, name='index'),
    path('drinks/<int:drink_id>', views.drinks_detail, name='detail'),
    path('drinks/create/', views.DrinkCreate.as_view(), name='drinks_create'),
    path('drinks/<int:pk>/update/', views.DrinkUpdate.as_view(), name='drinks_update'),
    path('drinks/<int:pk>/delete/', views.DrinkDelete.as_view(), name='drinks_delete'),
    path('drinks/<int:drink_id>/add_review/', views.add_review, name='add_review'),
]