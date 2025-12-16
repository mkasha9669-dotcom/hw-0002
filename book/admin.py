from django.contrib import admin
from .models import Author, Book, BookStore


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'nationality',
        'age',
        'created_at',
        'updated_at',
    )
    search_fields = ('first_name', 'last_name', 'nationality')
    list_filter = ('nationality',)
    ordering = ('first_name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'pages',
        'price',
        'cover_type',
        'total_sold',
        'in_stock',
        'created_at',
        'updated_at',
    )
    list_filter = ('cover_type', 'in_stock')
    search_fields = ('author__first_name', 'author__last_name')
    ordering = ('created_at',)


@admin.register(BookStore)
class BookStoreAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'seller',
        'total_sold',
        'created_at',
        'updated_at',
    )
    search_fields = ('name', 'address', 'seller__username')
    ordering = ('name',)
