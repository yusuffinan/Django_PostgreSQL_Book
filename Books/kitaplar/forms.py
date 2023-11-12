from django import forms
from django.forms import ModelForm
from kitaplar.models import Library

class CreateBook(ModelForm):
    class Meta:
        model = Library
        fields = '__all__'
  
       
class UpdateBook(ModelForm):
    class Meta:
        model = Library
        fields = '__all__'
  