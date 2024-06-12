from django.shortcuts import render
from app.models import Movies
from app.forms import Movieform
# Create your views here.

def home(request):
    m=Movies.objects.all()
    return render(request,template_name='card.html',context={'m':m})

def addmovies(request):
    if(request.method=='POST'):
        t=request.POST['title']
        i=request.POST['info']
        y=request.POST['year']
        c=request.FILES['cover']
        b=Movies.objects.create(title=t,info=i,year=y,cover=c)
        b.save()
        return home(request)
    return render(request,template_name='addbooks.html')

def movie(request,p):
    b=Movies.objects.get(id=p)
    return render(request,template_name='moreinfo.html',context={'m':b})

def delete(request,p):
    b=Movies.objects.get(id=p)
    b.delete()
    return home(request)


def edit(request,p):
    b=Movies.objects.get(id=p)

    if (request.method=='POST'):
        form=Movieform(request.POST,request.FILES,instance=b)
        if form.is_valid():
            form.save()
            return home(request)

    form=Movieform(instance=b)
    return render(request,template_name='edit.html',context={'form':form})



