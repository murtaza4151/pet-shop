from django.db import models
from django.contrib.auth.models import User
from product.models import product

# Create your models here.
class cart(models.Model):
    User=models.OneToOneField(User,on_delete=models.CASCADE)
    products=models.ManyToManyField(product,through="cartItem")

class cartitem(models.Model):
    cart=models.ForeignKey(cart,on_delete=models.CASCADE)
    products=models.ForeignKey(product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

class order(models.Model):
    order_id=models.CharField(max_length=200,primary_key=True,default="orderXYZ")
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    pincode=models.IntegerField()
    phoneno=models.CharField(max_length=10)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name}--{self.created_at}"  
    
class orderItem(models.Model):
    order=models.ForeignKey(order,on_delete=models.CASCADE)
    products=models.ForeignKey(product,on_delete=models.CASCADE)
    quantity=models.PositiveBigIntegerField(default=1)
    total=models.IntegerField()
