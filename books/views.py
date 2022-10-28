from rest_framework import generics
from .models import BookModel
from .serializers import BookModelSerializer, BookModelDetailSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

# Create your views here.

class BookDetailApiView(generics.RetrieveAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookModelDetailSerializer
    permission_classes = (AllowAny, )

class BookModelListAPIView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    
    def list(self, request, *args, **kwargs):
        queryset = BookModel.objects.all()
        serializer = BookModelSerializer(queryset, many = True)
        return Response({
            'books': serializer.data
        })