from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('books/create/', views.CreateBookView.as_view(), name='book-create'),
    path('books/update/<int:pk>/', views.UpdateBookView.as_view(), name='book-update'),
    path('books/delete/<int:pk>', views.DeleteBookView.as_view(), name='book-delete'),
]
