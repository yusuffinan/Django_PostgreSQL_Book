from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    cname=models.CharField(max_length=50)
    slug = models.SlugField(default="", db_index=True, null= False, unique=True, max_length=50)

    def __str__(self):
        return f"{self.cname}"
    
class Authorr(models.Model):
    aname=models.CharField(max_length=50)
    slug = models.SlugField(default="", db_index=True, null= False, unique=True, max_length=50)

    def __str__(self):
        return f"{self.aname}"

class Publisherr(models.Model):
    pname=models.CharField(max_length=50)
    slug = models.SlugField(default="", db_index=True, null= False, unique=True, max_length=50)

    def __str__(self):
        return f"{self.pname}"
    
# Create your models here.
class Library(models.Model):
    name= models.CharField(max_length=50)
    page_number = models.IntegerField()
    author = models.ForeignKey(Authorr, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="img/", default="")
    publisher = models.ForeignKey(Publisherr, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    summary = models.CharField(max_length=1000)
    slug = models.SlugField(default="", db_index=True, null= False, unique=True, max_length=50)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return f"{self.name}"

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user.username} - {self.library.name}"
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Library, on_delete=models.CASCADE)  # Burada Book, kitap modelinizi temsil etmelidir.
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.book.title} - {self.created_at}'