from django.urls import path 

from . import views 

""" urlpatterns = [ 
    path('hello/',views.hello_world),
    path('books/', views.books),
    path('books/<int:id>', views.book)
]  """
urlpatterns = [     
    path('books/', views.books.as_view()),
    path('books/<int:id>', views.book.as_view())
] 