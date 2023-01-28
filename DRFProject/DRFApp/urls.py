from django.urls import path 

from . import views 

urlpatterns = [ 
    path('hello/',views.hello_world),
    path('books/', views.books),
    path('books/<int:id>', views.book)
] 