from unicodedata import category
from rest_framework import generics
from .models import BookModel, CategoryModel
from .serializers import BookModelSerializer, BookModelDetailSerializer, CategoryModelSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework import filters

# Create your views here.

class CategoryBooksApiView(APIView):
    
    def get(self, request, pk, **kwargs):
        qs = BookModel.objects.filter(category=pk)
        serializer = BookModelSerializer(qs, many=True) 
        return Response({
            'books': serializer.data
        })


class BookDetailApiView(generics.RetrieveAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookModelDetailSerializer
    permission_classes = (AllowAny, )

class BookModelListAPIView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = BookModelSerializer
    filter_backends = [filters.SearchFilter, ]
    search_fields = ['title']
        
    def list(self, request, *args, **kwargs):
        queryset = BookModel.objects.all()
        cat_qs = CategoryModel.objects.all()
        serializer = BookModelSerializer(queryset, many = True)
        cat_serializer = CategoryModelSerializer(cat_qs, many=True)
        return Response({
            'books': serializer.data,
            'categories': cat_serializer.data
        })