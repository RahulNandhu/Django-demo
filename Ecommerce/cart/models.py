from django.db import models
from shop.models import Product
from django.contrib.auth.models import User

# Create your models here.

class Cart(models.Model):
    product= models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity= models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name


    def subtotal(self):
        return self.product.price * self.quantity


class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    no_of_item=models.IntegerField()
    address=models.TextField()
    phone=models.IntegerField()
    order_status=models.CharField(max_length=30,default='pending')
    delivery_status=models.CharField(max_length=30,default='pending')
    date_added=models.DateTimeField(auto_now_add=True)

    def Total(self):
        return self.no_of_item * self.product.price


    def __str__(self):
        return self.user.username

class Account(models.Model):
    acc_no=models.IntegerField()
    acc_type=models.CharField(max_length=30)
    amount=models.IntegerField()

    def __str__(self):
        return str(self.acc_no)
