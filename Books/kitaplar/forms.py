from django import forms
from django.forms import ModelForm, widgets
from kitaplar.models import Library, Comment

class CreateBook(ModelForm):
    class Meta:
        model = Library
        fields = '__all__'
  
       
class UpdateBook(ModelForm):
    class Meta:
        model = Library
        fields = '__all__'
  
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["text"].widget = widgets.TextInput(attrs={"class":"form-control"})