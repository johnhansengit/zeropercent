from django.shortcuts import render

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

drinks = [
  {'name': 'Sharab Rose Raspberry Shrub Cocktail', 'category': 'fruity', 'ingredients': 'simple syrup, raspberries, distilled white vinegar, rose water, sparkling water', 'difficulty': 3, 'prep': 80, 'img': 'https://www.foodandwine.com/thmb/tbrFoSya60adadsvNUpdLPiOcTY=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/Sharab-Rose-Raspberry-Shrub-XL-BLOG0623-9d7019eaf1654770a676608ca57e79ab.jpg'},
  {'name': 'Strawberry-Chile Balsamic Shrub', 'category': 'sweet and spicy', 'ingredients': 'strawberries, sugar, balsamic vinegar, chiles, sparkling water', 'difficulty': 3, 'prep': 150, 'img': 'https://www.foodandwine.com/thmb/GLC7Dq05YA8MPB6DPenYohKHUc4=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/Strawberry-Chili-Balsamic-Shrub-FT-RECIPE0423-df71d495016142f3b32f09235ae3924c.jpg'},
]

def drinks_index(request):
  return render(request, 'drinks/index.html', {
    'drinks': drinks
  })