from django import forms
from .models import Book

class DatePickerInput(forms.DateInput):
    input_type = 'date'

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author_key', 'published_date', 'pages', 'summary']
        widgets = {
            'published_date': DatePickerInput(format='%Y-%m-%d'),
        }