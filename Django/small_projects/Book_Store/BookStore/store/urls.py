from django.urls import path
from .views import store,delete,show,add_book

urlpatterns=[
    path('',store,name='index_store'),
    path('delete/<int:book_id>',delete,name='delete_book'),
    path('show/<int:book_id>',show,name='show_book'),
    path('add_book/',add_book,name='add_book')
]

