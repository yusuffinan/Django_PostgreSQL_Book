from django.http import Http404
from django.shortcuts import render

from kitaplar.models import Authorr, Category, Library

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

def details(request, id):
    try:
        book_detail = Library.objects.get(id=id)
    except:
        raise Http404("Bulumuyor")

    return render(request, "kitaplar/details.html", {"book_detail":book_detail})

def author_p(request, slug):
    books = Library.objects.filter(author__slug=slug)
    author_detail = Authorr.objects.all()
    return render(request, "kitaplar/author.html", {
        "book": books,
        "author_detail": author_detail
    })

def publisher_p(request,slug):
    pass
