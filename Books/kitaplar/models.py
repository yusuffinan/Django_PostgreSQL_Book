from django.db import models


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
    

