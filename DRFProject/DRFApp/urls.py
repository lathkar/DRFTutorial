from django.urls import path 

from . import views 
from .views import BookViewSet

""" urlpatterns = [ 
    path('hello/',views.hello_world),
    path('books/', views.books),
    path('books/<int:id>', views.book)
]  """
""" urlpatterns = [     
    path('books/', views.books.as_view()),
    path('books/<int:id>', views.book.as_view())
] """ 

""" book_list = BookViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
book_detail = BookViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
}) """
""" urlpatterns = [     
    path('books/list/', views.BookList.as_view()),
    path('books/new/', views.BookNew.as_view()),
    path('books/detail/<int:id>', views.BookDetail.as_view()),
    path('books/update/<int:id>', views.BookUpdate.as_view()),
    path('books/delete/<int:id>', views.BookDelete.as_view()),
    path('books/', views.books.as_view()),
    path('books/<int:id>', views.book.as_view()) 

] """

""" urlpatterns = [
    path('books/', book_list, name='book-list'),
    path('books/<int:pk>/', book_detail, name='book-detail')
] """