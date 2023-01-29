class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

#b1 = Book(title='Django', author='XYZ', price=200)

from rest_framework import serializers

class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=50)
    author = serializers.CharField(max_length=50)
    price = serializers.IntegerField()

""" ser_b1=BookSerializer(b1)
print (ser_b1.data)
 """
""" from rest_framework.renderers import JSONRenderer
json_b1 = JSONRenderer().render(ser_b1.data)
print (json_b1) """
