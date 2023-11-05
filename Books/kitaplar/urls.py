from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="kitaplar_index"),
    path('category_list', views.category, name="category_list"),
    path("kategori/<slug:slug>", views.getBooksByCategory, name="books_by")
]
