from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
""" def home(request):
    return render(request, 'index.html') """

from rest_framework.renderers import TemplateHTMLRenderer, AdminRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Book
from .serializers import BookSerializer

class booklist(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'booklist.html'
    def get(self, request):
        books=Book.objects.all()
        return Response({'books':books})

""" from rest_framework import viewsets

class BookViewSet(viewsets.ModelViewSet):
    
    renderer_classes = [AdminRenderer]
    queryset = Book.objects.all()
    serializer_class = BookSerializer """

class bookdetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'bookdetail.html'
	
    def get(self, request, id):
        book = Book.objects.get(pk=id)
        serialized_book = BookSerializer(book)
        return Response({'serializer': serialized_book, 'book': book})
		
    def post(self, request, id):
        book = get_object_or_404(Book, pk=id)
        serialized_book=BookSerializer(book, data=request.data)
        if not serialized_book.is_valid():
            return Response({'serializer': serialized_book, 'book': book})
        serialized_book.save()
        return redirect('book-list')
