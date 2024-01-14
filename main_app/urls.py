from django.urls import path
from . import views
	
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('recipes/', views.recipes_index, name='index'),
    path('recipes/<int:recipe_id>', views.recipes_detail, name='detail'),
    path('recipes/create/', views.RecipeCreate.as_view(), name='recipes_create'),
    path('recipes/<int:pk>/update/', views.RecipeUpdate.as_view(), name='recipes_update'),
    path('recipes/<int:pk>/delete/', views.RecipeDelete.as_view(), name='recipes_delete'),
    path('recipes/<int:recipe_id>/add_review/', views.add_review, name='add_review'),

    path('products/', views.ProductList.as_view(), name='products_index'),
    path('products/<int:pk>/', views.ProductDetail.as_view(), name='products_detail'),
    path('products/create/', views.ProductCreate.as_view(), name='products_create'),
    path('products/<int:pk>/update/', views.ProductUpdate.as_view(), name='products_update'),
    path('products/<int:pk>/delete/', views.ProductDelete.as_view(), name='products_delete'),

    path('places/<int:place_id>/assoc_product/<int:product_id>/', views.assoc_product, name='assoc_product'),
    path('places/<int:place_id>/disassoc_product/<int:product_id>/', views.disassoc_product, name='disassoc_product'),

    path('places/', views.PlaceList.as_view(), name='places_index'),
    path('places/<int:place_id>', views.places_detail, name='places_detail'),
    path('places/create/', views.PlaceCreate.as_view(), name='places_create'),
    path('places/<int:pk>/update/', views.PlaceUpdate.as_view(), name='places_update'),
    path('places/<int:pk>/delete/', views.PlaceDelete.as_view(), name='places_delete'),
]