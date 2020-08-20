from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import MoviesSerializer, CategorySerializer
from .models import Movies, Category


class MoviesViewSet(viewsets.ModelViewSet):
    queryset = Movies.objects.all().order_by('id')
    serializer_class = MoviesSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer