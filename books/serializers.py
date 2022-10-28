from rest_framework import serializers
from .models import BookModel, AuthorModel, BookImageModel, FeaturesModel

class FeaturesModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FeaturesModel
        fields = '__all__'

class BookImageModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BookImageModel
        fields = ['image']

class AuthorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = ['full_name']

class BookModelSerializer(serializers.ModelSerializer):
    author = AuthorModelSerializer()
    image = BookImageModelSerializer()
    
    class Meta:
        model = BookModel
        exclude = ['status', 'description', 'features', 'created_at', 'updated_at']
        
        
class BookModelDetailSerializer(serializers.ModelSerializer):
    author = AuthorModelSerializer()
    image = BookImageModelSerializer()
    features = FeaturesModelSerializer()
    
    class Meta:
        model = BookModel
        fields = '__all__'