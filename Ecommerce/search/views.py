from django.shortcuts import render
from shop.models import Product
from django.db.models import Q

# Create your views here.

def search(request):
    se=''
    result=None

    if request.method=='POST':
        se=request.POST['s']
        if se:
            result=Product.objects.filter(Q(name__icontains=se) | Q(desc__icontains=se))
    return render(request,template_name='search.html',context={'re':result,'se':se})
