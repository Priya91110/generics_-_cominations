from django.shortcuts import render
from rest_framework import generics
from .models import Car, CarSerializer
# Create your views here.
'''
CreateAPIView  ---- CreateModelMixin ---list()
ListAPIView
RetrieveAPIView
DestroyAPIView
UpdateAPIView


ListCreateAPIView
RetrieveUpdateAPIView
RetrieveDestroyAPIView
RetrieveUpdateDestroyAPIView
'''

'''
class CarListCreateView(generics.ListAPIView, generics.CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
'''
# or we can do like this
class CarListCreateView(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
'''    
class CarDetailView(generics.RetrieveAPIView, generics.DestroyAPIView, generics.UpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
'''    
# or we can do like this
class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    