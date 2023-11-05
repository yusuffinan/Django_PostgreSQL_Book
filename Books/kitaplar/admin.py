from django.contrib import admin
from .models import Library, Category

# Register your models here.
@admin.register(Library)
class BooksAdmin(admin.ModelAdmin):
    list_display = ("name", "page_number","author", "publisher","summary",)
    list_filter = ("name", "author","publisher",)
    search_fields = ("name", "summary",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("cname","slug",)
    prepopulated_fields = {"slug": ("cname",),}
    