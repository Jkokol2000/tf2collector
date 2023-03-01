from django.db import models
from django.urls import reverse
TRADE = (
    ('F', 'Free'),
    ('I', 'Items'),
    ('M', 'Money')
)

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    quality = models.CharField(max_length=100)
    effect = models.TextField(max_length=250)
    amount = models.IntegerField()
    
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("item", kwargs={"item_id": self.id})
    
class Request(models.Model):
    date = models.DateField('Trade Request Date')
    trade = models.CharField(
        max_length=1,
        choices=TRADE,
        default=TRADE[0][0])
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.get_trade_display()} on {self.date}"
    class Meta:
        ordering = ['-date']
    
    
   
    