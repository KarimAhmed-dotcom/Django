from django.shortcuts import render,redirect
from .models import Store
from .forms import BookForm
# Create your views here.
def index(request):
    data=Store.objects.all()
    return render(request,'store/index.html',context={'books':data})

def add_book(request):
    form=BookForm()
    if request.method=='POST':
        form=BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            form=BookForm(request.POST)
    
    return render(request,'store/add_book.html',context={'form':form})

def delete_book(request,id):
    Store.objects.get(pk=id).delete()
    return redirect('index')
    

def edit_book(request,id):
    book=Store.objects.get(pk=id)
    if request.method=='POST':
        form=BookForm(request.POST,instance=book)
        if form.is_valid():
            form.save()
            return redirect('index')
        else :
            form=BookForm(instance=book)
    
    form=BookForm(instance=book)
    return render(request,'store/edit_book.html',context={'form':form,'id':id})