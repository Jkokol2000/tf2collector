from django.contrib import admin
from .models import Item, Request, Player

# Register your models here.
admin.site.register(Item)
admin.site.register(Request)
admin.site.register(Player)