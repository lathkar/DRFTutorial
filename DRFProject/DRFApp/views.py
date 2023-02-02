from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer

""" @api_view()
def hello_world(request):
    return Response({"message": "Hello, world!"})

@api_view(['GET','POST']) 
def books(request): 
    if request.method=='GET':
        books = Book.objects.all()
        serialized_books = BookSerializer(books, many=True)
        return Response(serialized_books.data)
    elif request.method=='POST':
        serialized_book = BookSerializer(data=request.data)
        serialized_book.is_valid(raise_exception=True)
        serialized_book.save()
        return Response(serialized_book.validated_data,status.HTTP_201_CREATED)

@api_view(['GET','PUT', 'DELETE'])
def book(request, id):
    book = Book.objects.get(pk=id)
    if request.method=='GET':
        
        serialized_book = BookSerializer(book)
        return Response(serialized_book.data)
    elif request.method=='PUT':
        book.price = request.data['price']
        book.save()
        serialized_book=BookSerializer(book)
        return Response(serialized_book.data) """
from rest_framework.views import APIView

""" class books(APIView):
    def get(self, request):
        books = Book.objects.all()
        serialized_books = BookSerializer(books, many=True)
        return Response(serialized_books.data)
    def post(self, request):
        serialized_book = BookSerializer(data=request.data)
        serialized_book.is_valid(raise_exception=True)
        serialized_book.save()
        return Response(serialized_book.validated_data,status.HTTP_201_CREATED)

class book(APIView):
    def get(self, request, id):
        book = Book.objects.get(pk=id)
        serialized_book = BookSerializer(book)
        return Response(serialized_book.data)
    def put(self, request, id):
        book = Book.objects.get(pk=id)
        book.price = request.data['price']
        book.save()
        serialized_book=BookSerializer(book)
        return Response(serialized_book.data)
    def delete(self, request, id):
        book = Book.objects.get(pk=id)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
 """
from rest_framework import generics

""" class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveAPIView):
    lookup_field = 'id' 
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookUpdate(generics.UpdateAPIView):
    lookup_field = 'id' 
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDelete(generics.DestroyAPIView):
    lookup_field = 'id' 
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookNew(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class books(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class book(generics.RetrieveUpdateDestroyAPIView):
    lookup_field='id'
    queryset = Book.objects.all()
    serializer_class = BookSerializer """

from rest_framework import viewsets

class BookViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer