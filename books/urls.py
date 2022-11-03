from django.urls import path
from . views import BookDetailApiView, BookModelListAPIView, CategoryBooksApiView, CategoryListApiView

urlpatterns = [
    path('books/', BookModelListAPIView.as_view(), name='books_list'),
    path('books/<int:pk>/', BookDetailApiView.as_view(), name='book_detail'),
    path('books/cat/<int:pk>/', CategoryBooksApiView.as_view(), name='book_detail_category'),
    path('categories/', CategoryListApiView.as_view(), name='category_list'),
]
