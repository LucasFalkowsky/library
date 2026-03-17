from django.contrib import admin
from . import models

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author_key', 'cover')

admin.site.register(models.Author)
admin.site.register(models.Genre)