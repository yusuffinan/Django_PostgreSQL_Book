from django.contrib import admin
from .models import Favorite, Library, Category, Authorr, Publisherr, Comment

# Register your models here.
@admin.register(Library)
class BooksAdmin(admin.ModelAdmin):
    list_display = ("name", "page_number","summary",)
    list_filter = ("name", "author","publisher",)
    search_fields = ("name", "summary",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("cname","slug",)
    prepopulated_fields = {"slug": ("cname",),}

@admin.register(Authorr)
class AuthorrAdmin(admin.ModelAdmin):
    list_display = ("aname","slug")
    prepopulated_fields = {"slug": ("aname",),}

@admin.register(Publisherr)
class PublisherrAdmin(admin.ModelAdmin):
    list_display = ("pname","slug")
    prepopulated_fields = {"slug": ("pname",),}

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ("user","library")
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("user","book")