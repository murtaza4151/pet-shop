from django.contrib import admin
from django.urls import path
from . import views

urlpatterns= [
    path("add-to-cart/<int:productId>",views.add_to_cart,name="add_to_cart"),
    path("cart/",views.view_cart,name="view_cart"),
    path("cart/update/<int:cartItemId>/",views.update_cart,name="updatecart"),
    path("cart/delete/<int:cartItemId>",views.delete_cart,name="deletecartItem"),
    path("checkout/",views.check_out,name="checkout"),
    path("payment/<str:orderId>",views.make_payment,name="payment") 
    


]
