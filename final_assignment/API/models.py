from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    title = models.CharField(max_length=255 , db_index=True)
    slug = models.SlugField()

class MenuItem(models.Model):
    title = models.CharField(max_length=255,db_index=True)
    price = models.DecimalField(max_digits=6, decimal_places=2 , db_index=True)
    featured = models.BooleanField(db_index=True)
    Category = models.ForeignKey(Category ,on_delete=models.PROTECT)

class Card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    
   

    class Meta:
        unique_together = ('user', 'menu_item')    


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(db_index=True,default=False)
    total = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True,db_index=True)
    delivery_crew = models.ForeignKey(User, related_name='delivery_crew', on_delete=models.SET_NULL ,null=True)



class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ('order', 'menu_item')

