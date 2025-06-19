from django.urls import path
from .views import index,delete_book,add_book,edit_book


urlpatterns=[
    path('',index,name='index'),
    path('delete/<int:id>',delete_book,name='delete_book'),
    path('add_book',add_book,name='add_book'),
    path('edit_book/<int:id>',edit_book,name="edit_book")
]