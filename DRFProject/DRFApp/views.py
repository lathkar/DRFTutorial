from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer

@api_view()
def hello_world(request):
    return Response({"message": "Hello, world!"})

@api_view() 
def books(request): 
    books = Book.objects.all()
    serialized_books = BookSerializer(books, many=True)
    return Response(serialized_books.data)