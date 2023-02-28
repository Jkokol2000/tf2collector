from django.shortcuts import render
from .models import Item

# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')
def about(request):
    return render(request, 'about.html') 
def items_index(request):
  items = Item.objects.all()
  # We pass data to a template very much like we did in Express!
  return render(request, 'items/index.html', {
    'items': items
  })
  