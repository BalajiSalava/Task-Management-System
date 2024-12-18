from django.shortcuts import render,redirect
from myapp.models import Task,Restore
from .forms import Aboutf
from .models import About
# Create your views here.
def Home(request):
    read=Task.objects.all()
    data={'data':read}
    return render(request,'home.html',data)


def Create(request):
    if request.method=='POST':
        Title=request.POST['Title']
        Disc=request.POST['Disc']
        Task.objects.create(Title=Title,Disc=Disc)
        return redirect('home')
    return render(request,'create.html')



def Dele(request,id):
    b=Task.objects.get(id=id)
    c=Restore.objects.create(Title=b.Title,Disc=b.Disc)
    c.save()
    b.delete()
    return redirect('home')


def History(request):
    b=Restore.objects.all()
    return render(request,'history.html',{'data':b})


def Update(request,id):
    s=Task.objects.get(id=id)
    if request.method=='POST':
        s.Title=request.POST['Title']
        s.Disc=request.POST['Disc']
        s.save()
        return redirect('home')
        
        
    return render(request,'create.html',{'data':s})
    
def restore(request,id):
    b=Restore.objects.get(id=id)
    a=Task.objects.create(Title=b.Title,Disc=b.Disc)
    b.delete()
    a.save()
    return redirect('history')



def del_restore(request,id):
    b=Restore.objects.get(id=id)
    b.delete()
    return redirect('history')

def restoreall(request):
    a=Restore.objects.all()
    for i in a:
        Title=i.Title
        Disc=i.Disc
        b=Task.objects.create(Title=Title,Disc=Disc)
        b.save()
    a.delete()
    return redirect('history')

def deleteall(request):
    a=Restore.objects.all()
    a.delete()
    return redirect('history')

def about(request):
    a= Aboutf
    if request.method=='POST':
        name=request.POST['name']
        contact=request.POST['contact']
        email=request.POST['email']
        suggestions=request.POST['suggestions']
        About.objects.create(name=name,contact=contact,email=email,suggestions=suggestions)
    return render(request,'about.html',{'a':a})