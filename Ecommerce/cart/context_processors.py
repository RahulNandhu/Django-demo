from .models import Cart
def total(request):
    item_count=0
    if request.user.is_authenticated:
        u=request.user
        try:
            c = Cart.objects.filter(user=u)
            for i in c:
                item_count +=i.quantity
        except:
            item_count=0
    return{'count':item_count}