from django.shortcuts import redirect, render
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from .models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def main(request):
    return render(request,'accounts/main.html')

def list(request):
    lists = User.objects.all()
    context = {
        'lists':lists,
    }
    return render(request,'accounts/list.html',context)

def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('accounts:main')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html',context)

def detail(request, pk):
    user = get_user_model.objects.get(pk=pk)
    context = {
        'user':user
    }
    return render(request,'accounts/detail.html',context)

def login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'review:index')
    else:
        form = AuthenticationForm()
    context = {
        'form':form,
    }
    return render(request,'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('review:index')