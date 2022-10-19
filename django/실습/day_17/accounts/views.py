from django.shortcuts import redirect, render
from .models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
def login(request):
    if request.method == "POST":
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            auth_login(request, login_form.get_user())
            return redirect('accounts:index')
    else:
        login_form = AuthenticationForm()
    
    context = {
        'login_form': login_form,
    }
    return render(request,'accounts/login.html', context)

def index(request):
    return render(request, 'accounts/index.html')

def logout(request):
    auth_logout(request)
    return redirect('accounts:index')

def detail(request, accounts_pk):
    article = User.objects.get(pk=accounts_pk)
    context = {
        'article': article,
    }
    return render(request, 'accounts/detail.html', context)