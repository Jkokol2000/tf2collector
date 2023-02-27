from django.shortcuts import render

# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')
def about(request):
    return render(request, 'about.html') 
def items_index(request):
  # We pass data to a template very much like we did in Express!
  return render(request, 'items/index.html', {
    'items': items
  })
  
items = [
      {'name': 'Team Captain', 'quality' : 'Unusual', 'effect' : 'Burning Flames', 'amount' : 1},
      {'name': 'Sandman', 'quality' : 'Strange', 'effect' : 'None', 'amount' : 2}
]