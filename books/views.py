from unicodedata import category
from rest_framework import generics
from .models import BookModel, CategoryModel
from .serializers import BookModelSerializer, BookModelDetailSerializer, CategoryModelSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework import filters
from .paginations import BooksPagination
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class CategoryListApiView(generics.ListAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategoryModelSerializer
    permission_classes = [AllowAny, ]
    pagination_class = None

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
    queryset = BookModel.objects.all()
    serializer_class = BookModelSerializer
    filter_backends = [DjangoFilterBackend,]
    filterset_fields = ('title', )
    pagination_class = BooksPagination
        
