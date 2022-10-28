from django.urls import path
from . views import BookDetailApiView, BookModelListAPIView

urlpatterns = [
    path('books/', BookModelListAPIView.as_view(), name='books_list'),
    path('books/<int:pk>/', BookDetailApiView.as_view(), name='book_detail'),
]
