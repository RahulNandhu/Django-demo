from django.shortcuts import render,HttpResponse
from .models import Category,Product
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def allcategory(request):
    da=Category.objects.all()
    return render(request,template_name='category.html',context={'data':da})

@login_required
def products(request,p):
    i=Category.objects.get(name=p)
    c=Product.objects.filter(category=i)
    return render(request,template_name='products.html',context={'i':i,'c':c})

@login_required
def details(request,p):
    i=Product.objects.get(id=p)
    return render(request,template_name='details.html',context={'i':i})


def register(request):
    if request.method=='POST':
        n=request.POST['uname']
        f = request.POST['fname']
        l = request.POST['lname']
        e = request.POST['email']
        p = request.POST['pass']
        cp = request.POST['cpass']

        if p==cp:
            user=User.objects.create_user(username=n,password=p,email=e,first_name=f,last_name=l)
            user.save()
            return allcategory(request)
        else:
            return HttpResponse('Passwords  are incorrect')
    return render(request,template_name='register.html')


def u_login(request):
    if request.method=='POST':
        u=request.POST['uname']
        p=request.POST['pass']

        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return allcategory(request)
        else:
            return HttpResponse('Invalid credentials')

    return render(request,template_name='login.html')

@login_required
def u_logout(request):
    logout(request)
    return u_login(request)