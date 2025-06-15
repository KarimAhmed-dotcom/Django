from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
# Create your views here.

all_books=[{
    'id':0,
    'name':'7habits',
    'salary':'200 EGP',
    'avilable':True,
    'img':'https://th.bing.com/th/id/OIP.vbkbYWYTtfy8wwNsbxi3pwHaE8?w=292&h=195&c=7&r=0&o=7&pid=1.7&rm=3'
    },{
    'id':1,
    'name':'fostok',
    'salary':'300 EGP',
    'avilable':True,
    'img':'https://th.bing.com/th/id/OIP.pgwLurxXcxhAVNwJH5GYRQHaFj?w=248&h=186&c=7&r=0&o=7&pid=1.7&rm=3'
    },{
    'id':2,
    'name':'prayer first',
    'salary':'500 EGP',
    'avilable':True,
    'img':'https://th.bing.com/th/id/OIP.LTr6jaxHlQl3Pg-9HwBGCQHaFj?w=248&h=186&c=7&r=0&o=7&pid=1.7&rm=3'
    },{
    'id':3,
    'name':'money',
    'salary':'100 EGP',
    'avilable':False,
    'img':'https://th.bing.com/th/id/OIP.o38DlWAQJhc0CNnDoEnF3AHaFj?w=230&h=186&c=7&r=0&o=7&pid=1.7&rm=3'
},{
    'id':4,
    'name':'science',
    'salary':'200 EGP',
    'avilable':True,
    'img':'https://th.bing.com/th/id/OIP.uyio8OJqqELflVbFaA6HvAHaE8?w=258&h=180&c=7&r=0&o=7&pid=1.7&rm=3'
},{
    'id':5,
    'name':'pysics',
    'salary':'100 EGP',
    'avilable':True,
    'img':'https://th.bing.com/th/id/OIP.9JYwdkoCWNvoRbsuP9CLuwHaE7?w=270&h=180&c=7&r=0&o=7&pid=1.7&rm=3'
},{
    'id':6,
    'name':'geography',
    'salary':'300 EGP',
    'avilable':False,
    'img':'https://th.bing.com/th/id/OIP.Mvjyv5dXZur6foZ518cynwHaFj?w=254&h=191&c=7&r=0&o=7&pid=1.7&rm=3'
},{
    'id':7,
    'name':'math',
    'salary':'100 EGP',
    'avilable':True,
    'img':'https://th.bing.com/th/id/OIP.LTr6jaxHlQl3Pg-9HwBGCQHaFj?w=254&h=191&c=7&r=0&o=7&pid=1.7&rm=3'
}]

def get_book(id):
    for book in all_books :
        if book['id']==id:
            return book

def store(request):
    return render(request,'store/index.html',context={
        'all_books':all_books
    }) 
    
def delete(request,book_id):
    book=get_book(book_id)
    all_books.remove(book)
    return redirect('index_store')

def show(request,book_id):
    book=get_book(book_id)
    return render(request,'store/show_book.html',context={
        'book':book
    })


def add_book(request):
    if request.method == "POST":
        id = request.POST.get("id")
        name = request.POST.get("name")
        salary = request.POST.get("salary")
        available = request.POST.get("avilable") == "True"
        img = request.POST.get("img")    
    
        all_books.append({
            'id':int(id),
            'name':name,
            'salary':f'{salary} EGP',
            'avilable':available,
            'img':img or 'https://th.bing.com/th/id/OIP.LTr6jaxHlQl3Pg-9HwBGCQHaFj?w=254&h=191&c=7&r=0&o=7&pid=1.7&rm=3'
        })
        return redirect('index_store')
    
    return render(request, "store/add_book.html",{})