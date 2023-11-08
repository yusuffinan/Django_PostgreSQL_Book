from django.forms import widgets
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget = widgets.TextInput(attrs={"class":"form-control"})
        self.fields["password"].widget = widgets.PasswordInput(attrs={"class":"form-control"})

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username","email","first_name","last_name")
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget = widgets.TextInput(attrs={"class":"form-control"})
        self.fields["password1"].widget = widgets.PasswordInput(attrs={"class":"form-control"})
        self.fields["password2"].widget = widgets.PasswordInput(attrs={"class":"form-control"})
        self.fields["email"].widget = widgets.EmailInput(attrs={"class":"form-control"})
        self.fields["first_name"].widget = widgets.TextInput(attrs={"class":"form-control"})
        self.fields["last_name"].widget = widgets.TextInput(attrs={"class":"form-control"})


