from django.shortcuts import render,HttpResponse
from shop.models import Product
from .models import Cart,Account,Order
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def addtocart(request,p):
    pro=Product.objects.get(name=p)
    u=request.user #to get current user details
    try:
        cart=Cart.objects.get(user=u,product=pro)
        if (cart.product.stock>0):
            cart.quantity += 1
            pro.stock -=1 #remove from the stock
            pro.save()
            cart.save()

    except:
        if (pro.stock >0):
            cart=Cart.objects.create(product=pro,user=u,quantity=1)
            cart.save()
            pro.stock -= 1  # remove from the stock
            pro.save()
    return cartview(request)

@login_required
def cartview(request):
    u=request.user
    c=Cart.objects.filter(user=u)
    k=0
    for j in c:
        k +=j.quantity * j.product.price
    return render(request, template_name='cartview.html',context={'cart':c,'total':k})

@login_required
def removecart(request,p):
    it=Product.objects.get(name=p)
    u=request.user
    try:
        cart=Cart.objects.get(product=it,user=u)
        if cart.quantity ==1:
            it.stock +=1 #adding to the stock
            it.save()
            cart.delete()
        else:
            cart.quantity -=1
            cart.save()
            it.stock += 1  # adding to the stock
            it.save()
    except:
        pass
    return cartview(request)

@login_required
def cartdelete(request,p):
    it = Product.objects.get(name=p)
    u = request.user
    cart=Cart.objects.get(user=u,product=it)
    it.stock += cart.quantity
    it.save()
    cart.delete()
    return cartview(request)

@login_required
def orderform(request):
    if request.method=='POST':
        a=request.POST['add']
        p = request.POST['ph']
        ac = request.POST['ac']

        u=request.user
        cart=Cart.objects.filter(user=u)

        bill_amount=0
        for i in cart:
            bill_amount +=i.quantity * i.product.price

        try:
            account=Account.objects.get(acc_no=ac)
            if (account.amount >= bill_amount):
                account.amount -=bill_amount
                account.save()
                for i in cart:
                    order=Order.objects.create(user=u,address=a,no_of_item=i.quantity,product=i.product,phone=p,order_status='ordered')
                    order.save()
                    msg='Order delivered'
                cart.delete()
            else:
                msg='Insufficient balance'

            return render(request,template_name='orderdetails.html',context={'msg':msg})
        except:
            msg='invalid bankdetails'
            return render(request,template_name='orderdetails.html',context={'msg':msg})

    return render(request,template_name='orderform.html')

@login_required
def yourorders(request):
    u=request.user
    items=Order.objects.filter(user=u)
    return render(request,template_name='ordered_items.html',context={'items':items})