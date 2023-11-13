from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse
from kitaplar.forms import CreateBook, UpdateBook, CommentForm
from kitaplar.models import Authorr, Category, Favorite, Library, Publisherr, Comment

# Create your views here.
def isAdmin(user):
    return user.is_superuser

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

# def details(request, id):
#     try:
#         book_detail = Library.objects.get(id=id)
#     except:
#         raise Http404("Bulumuyor")

#     return render(request, "kitaplar/details.html", {"book_detail":book_detail})
def details(request, id):
    book = get_object_or_404(Library, pk=id)
    comments = Comment.objects.filter(book=book)
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.book = book
            comment.save()
            return redirect('detay', id=id)  # Aynı sayfaya yönlendirme

    return render(request, 'kitaplar/details.html', {'book': book, 'comments': comments, 'form': form})

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


@user_passes_test(isAdmin)
def creates(request):
    if request.method == "POST":
        form = CreateBook(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("category_list")
        else:
            return render(request, "kitaplar/create.html", {"form": form})
    else:
        form = CreateBook()
    return render(request, "kitaplar/create.html", {"form": form})

@user_passes_test(isAdmin)
def deleted(request, id):
    form = get_object_or_404(Library, pk =id)
    if request.method == "POST":
        form.delete()
        return redirect("category_list")
    return render(request, "kitaplar/delete.html", {"form":form})

@user_passes_test(isAdmin)
def updated(request, id):
    kitap = get_object_or_404(Library, pk =id)
    if request.method == "POST":
        form = UpdateBook(request.POST, request.FILES, instance=kitap)
        if form.is_valid():
            form.save()
            detay_url = reverse("detay", args=[id])
            return redirect(detay_url)
    else:
        form = UpdateBook(instance=kitap)
    return render(request, "kitaplar/update.html", {"form":form})