from django.urls import path
from . import views


urlpatterns = [
    path('books/', views.booklist.as_view(), name='book-list'),
    path('books/<int:id>', views.bookdetail.as_view(), name='book-detail')
]