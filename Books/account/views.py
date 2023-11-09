from django.shortcuts import redirect, render
from  .forms import LoginForm, RegisterForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from .models import Profile
from django.contrib.auth.decorators import login_required
# Create your views here.

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request, data = request.POST)
        if form.is_valid():
            username= form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)

                return redirect("category_list")
        else:
            return render(request, "account/login.html", {"form": form})
    else:
        form = LoginForm()
        return render(request, "account/login.html", {"form": form})


def user_register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # Kullanıcıyı kaydet
            # Kullanıcı kaydı tamamlandığında profil nesnesini oluşturun
            profile = Profile(user=user, profile_picture='varsayilan.jpg')
            profile.save()
            login(request, user)  # Kullanıcıyı oturum açmış olarak işaretleyin
            return redirect("login_")  # Başka bir sayfaya yönlendirme yapabilirsiniz
        else:
            return render(request, "account/register.html", {"form": form})
    else:
        form = RegisterForm()
        return render(request, "account/register.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("login_")

@login_required
def user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile_')  # Profil sayfasına yönlendirme yapabilirsiniz
    else:
        form = UserProfileForm()
    
    return render(request, 'account/profile.html', {'form': form})