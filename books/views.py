from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
import copy

from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from . import models
from .forms import BookForm

def calc_reading_time(book):
    try:
        return f'{round(book.pages / 30, 1)} Stunden'
    except ZeroDivisionError:
        return 'Keine Lesedauer angegeben'
    except TypeError:
        return 'Keine Lesedauer angegeben'
    except Exception as e:
        return f'Fehler: {e}'

class BookListView(ListView):
    model = models.Book
    context_object_name = 'books'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for book in context['books']:
            book.reading_time = calc_reading_time(book)
        return context

class BookDetailView(DetailView):
    model = models.Book
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = context['book']
        book.reading_time = calc_reading_time(book)
        return context

class CreateBookView(CreateView):
    model = models.Book
    form_class = BookForm

    def get_success_url(self):
        return reverse('book-detail', kwargs={'pk': self.object.pk})

class UpdateBookView(UpdateView):
    model = models.Book
    form_class = BookForm

    def get_success_url(self):
        return reverse('book-detail', kwargs={'pk': self.object.pk})

class DeleteBookView(DeleteView):
    model = models.Book

    def get_success_url(self):
        return reverse('book-list')
