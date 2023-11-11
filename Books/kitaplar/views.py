from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from kitaplar.forms import CreateBook
from kitaplar.models import Authorr, Category, Favorite, Library, Publisherr

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
    books = Library.objects.filter(publisher__slug=slug)
    publisher_detail = Publisherr.objects.all()
    return render(request, "kitaplar/publisher.html", {
        "book": books,
        "author_detail": publisher_detail
    })

def search(request):
    if 'q' in request.GET and request.GET['q'] != '':
        q = request.GET['q']
        kategori = Category.objects.all()
        books_list = Library.objects.filter(name__contains=q) | Library.objects.filter(
            author__aname__contains=q) | Library.objects.filter(publisher__pname__contains=q)
    else:
        return redirect("category_list")
    return render(request, 'kitaplar/search.html', {

        "categories":kategori,
        "books_list":books_list
        })

@login_required
def favorite(request, id):
    library = get_object_or_404(Library, pk=id)
    created = Favorite.objects.get_or_create(user=request.user, library=library)
    user_favorites = Favorite.objects.filter(user=request.user)  # Kullanıcının tüm favori kitapları
    return render(request, "kitaplar/favorite.html", {"library": library, "created": created, "user_favorites": user_favorites})

@login_required
def creates(request):
    if request.method == "POST":
        form = CreateBook(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            return redirect("category_list")
    else:
        form = CreateBook()
    return render(request, "kitaplar/create.html",{"form":form})