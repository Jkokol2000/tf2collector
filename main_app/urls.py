from django.urls import path
from . import views
	
urlpatterns = [
	path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('items/', views.items_index, name='index'),
    path('items/<int:item_id>/', views.items_detail, name='item'),
    path('items/create/', views.ItemCreate.as_view(), name='item_create'),
    path('items/<int:pk>/update/', views.ItemUpdate.as_view(), name='item_update'),
    path('items/<int:pk>/delete/', views.ItemDelete.as_view(), name='item_delete'),
    path('cats/<int:item_id>/add_request/', views.add_request, name='add_request'),
    path('players/<int:item_id>/assoc_player/<int:player_id>/', views.assoc_player, name='assoc_player'),
    path('players/', views.PlayerList.as_view(), name = 'players_index'),
    path('players/<int:pk>/', views.PlayerDetail.as_view(), name = 'players_detail'),
    path('players/create/', views.PlayerCreate.as_view(), name = 'players_create'),
    path('players/<int:pk>/update/', views.PlayerUpdate.as_view(), name = 'players_update'),
    path('players/<int:pk>/delete/', views.PlayerDelete.as_view(), name = 'players_delete'),
]