from rest_framework import serializers

from .models import Movies, Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id','category']

class MoviesSerializer(serializers.ModelSerializer):

    category = CategorySerializer
    
    class Meta:
        model = Movies
        fields = ['id','moviename','rating', 'category']

