from django.shortcuts import render

from kitaplar.models import Category, Library

# Create your views here.

def index(request):
    return render(request, 'kitaplar/index.html')
def category(request):
    kategori = Category.objects.all()
    books_list = Library.objects.all()
    return render(request, 'kitaplar/category_list.html', {
        "categories":kategori,
        "books_list":books_list
        })
def getBooksByCategory(request, slug):
    books_list = Library.objects.filter(categories__slug=slug)
    kategori = Category.objects.all()
    return render(request, 'kitaplar/category_list.html', {
        "categories":kategori,
        "books_list":books_list,
        "selected_category": slug
        })


