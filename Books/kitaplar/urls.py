from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="kitaplar_index"),
    path('category_list', views.category, name="category_list"),
    path("kategori/<slug:slug>", views.getBooksByCategory, name="books_by"),
    path('detay/<int:id>', views.details, name="detay"),
    path('yazarsayfasi/<slug:slug>',views.author_p, name="yazarsayfasi"),
    path('yayinevi/<slug:slug>',views.publisher_p, name="yayinevi")

]
