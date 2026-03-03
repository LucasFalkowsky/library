from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list),
    path('books/<int:pk>/', views.book_detail),
    path('genre_books/<str:genre_name>/', views.genre_detail),
]
