from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Author(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    def __str__(self):
        # return f"{self.firstname} {self.lastname}"
        return self.firstname + " " + self.lastname

class Book(models.Model):
    title = models.CharField(max_length=200)
    # blank=True (Kann leer gelassen werden)
    # null=True (Kann auch wieder auf "leer" gesetzt werden)
    # on_delete=models.SET_NULL (Ist nicht definiert, wenn Autor gelöscht wird)
    author_key = models.ForeignKey(Author, blank=True, null=True, on_delete=models.SET_NULL)
    published_date = models.DateField()
    pages = models.IntegerField()
    summary = models.TextField()
    genre = models.ManyToManyField(Genre, blank=True)
    isbn = models.IntegerField()

    def __str__(self):
        return f'{self.title} von {self.author_key}'