from django.shortcuts import render, redirect
from django.views.generic.edit import *
from django.views.generic import *
from .models import Item, Player
from .forms import RequestForm

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
def items_detail(request, item_id):
    item = Item.objects.get(id=item_id)
    id_list = item.players.all().values_list('id')
    unassigned_players = Player.objects.exclude(id__in=id_list)
    request_form = RequestForm()
    return render(request, 'items/details.html', { 'item' : item, 'request_form': request_form, 'players': unassigned_players})
def add_request(request, item_id):
    form = RequestForm(request.POST)
    if form.is_valid():
        new_request = form.save(commit=False)
        new_request.item_id = item_id
        new_request.save()
    return redirect('item', item_id=item_id)
def assoc_player(request, player_id, item_id):
    Item.objects.get(id=item_id).players.add(player_id)
    return redirect('item', item_id=item_id)
class ItemCreate(CreateView):
    model = Item
    fields = '__all__'
    success_url = '/items'
class ItemUpdate(UpdateView):
    model = Item
    fields = '__all__'
class ItemDelete(DeleteView):
    model = Item
    success_url = '/items'
class PlayerList(ListView):
    model = Player
class PlayerDetail(DetailView):
    model = Player
class PlayerCreate(CreateView):
    model = Player
    fields = '__all__'    
class PlayerUpdate(UpdateView):
    model = Player
    fields = '__all__'
class PlayerDelete(DeleteView):
    model = Player
    success_url = '/players'