from django.shortcuts import render
import copy
from . import models

def book_list(request):
    all_books = models.Book.objects.all()
    all_genres = models.Genre.objects.all()
    authors = [b.author_key for b in all_books]
    unique_authors = set(authors)
    genre_names = [genre.name.upper() for genre in all_genres]

    formated_books = []
    for book in all_books:
        formated_book = book
        formated_book.published_date = formated_book.published_date.strftime('%d.%m.%Y')
        formated_books.append(formated_book)

    return render(request, 'books/book_list.html', {'books':formated_books, 'genres':genre_names, 'authors':unique_authors})

def calc_reading_time(book):
    try:
        return f'{round(book.pages / 30, 1)} Stunden'
    except ZeroDivisionError:
        return 'Keine Lesedauer angegeben'
    except TypeError:
        return 'Keine Lesedauer angegeben'
    except Exception as e:
        return f'Fehler: {e}'

def book_detail(request, pk):
    book = models.Book.objects.get(pk=pk)

    book_new = copy.deepcopy(book)
    book_new.reading_time = calc_reading_time(book)

    return render(request, 'books/book_detail.html', {'book':book_new})

def genre_detail(request, genre_name):
    genre_books = models.Book.objects.filter(genre__name__icontains=genre_name).distinct()

    return render(request, 'books/genre_detail.html', {'books':genre_books})
