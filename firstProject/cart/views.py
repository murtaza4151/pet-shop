from operator import itemgetter
import random
from typing import ItemsView
from urllib import request
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, HttpResponse, render
from product.models import product
from .models import cartitem, orderItem
from .models import cart

# Create your views here.

def add_to_cart(request,productId):
    # logic for adding cart
    products=get_object_or_404(product,id=productId)
    print(products.product_name)
    #fetching current user
    currentUser=request.user

    carts,created= cart.objects.get_or_create(User=currentUser)
    print(created)
    item,item_created=cartitem.objects.get_or_create(cart=carts,products=products)


    
    quantity=request.GET.get("quantity")

    if not item_created:
        print(type(quantity))
        item.quantity+=int(quantity)
    else:
        cartitem.quantity=1

    item.save()
    return HttpResponseRedirect("/p/productlookup/")

def view_cart(request):
    currentUser=request.user
    carts,created=cart.objects.get_or_create(User=currentUser)
    cartitem=carts.cartitem_set.all()
    print(cartitem)
    finalAmount=0

    for item in cartitem:
        finalAmount+=item.quantity*item.products.product_price

    return render(request,"cart.html",{"items":cartitem,"finalamount":finalAmount})


def update_cart(request,cartItemId):
    cartItem=get_object_or_404(cartitem,pk=cartItemId)
    quantity=request.GET.get("quantity")
    cartItem.quantity=int(quantity)
    cartItem.save()
    return HttpResponseRedirect("/cart/")

def delete_cart(request,cartItemId):
    cartItem=get_object_or_404(cartitem,pk=cartItemId)
    cartItem.delete()
    return HttpResponseRedirect("/cart/")

from .forms import orderforms
from.models import order,orderItem
import uuid
def check_out(request):
    currentUser=request.user
    initial={
        "user":currentUser,
        "first_name":currentUser.get_short_name(),
        "last_name":currentUser.last_name
    }
    form=orderforms(initial=initial)
    carts,created=cart.objects.get_or_create(User=currentUser)
    cartitem=carts.cartitem_set.all()
    print(cartitem)
    finalAmount=0

    for item in cartitem:
        finalAmount+=item.quantity*item.products.product_price

    if request.method=="POST":
        form=orderforms(request.POST)
        if form.is_valid():
            user=form.cleaned_data['user']
            firstName=form.cleaned_data['first_name']
            lastName=form.cleaned_data['last_name']
            address=form.cleaned_data['address']
            city=form.cleaned_data['city']
            state=form.cleaned_data['state']
            pincode=form.cleaned_data['pincode']
            phoneno=form.cleaned_data['phoneno']
            

            orderid=str(uuid.uuid4())

            orders=order.objects.create(user=user,first_name=firstName,
                                 last_name=lastName,
                                 address=address,
                                 city=city,
                                 state=state,
                                 pincode=pincode,
                                 phoneno=phoneno,
                                 order_id=orderid[:8]
                                 )
            
            for item in cartitem:
                orderItem.objects.create(
                    order=orders,
                    products=item.products,
                    quantity=item.quantity,
                    total=item.quantity*item.products.product_price
                )
            

        return HttpResponseRedirect("/payment/"+orderid[:8])
    return render(request,"checkout.html",{"form":form,"items":cartitem,"finalAmount":finalAmount})
import razorpay
def make_payment(request,orderId):
    orders=order.objects.get(pk=orderId)
    orderItem=orders.orderitem_set.all()
    amount=0
    for item in orderItem:
        amount+=item.total

    print(amount)

    return render(request,"payment.html",{})


