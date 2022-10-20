from django.shortcuts import redirect, render
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def signup(request):
    if request.method == "POST":
        signup_form = CustomUserCreationForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            return redirect('articles:index')
    else:
        signup_form = CustomUserCreationForm()
    context = {
        'signup_form':signup_form,
    }
    return render(request, 'accounts/signup.html',context)

def detail(request, accounts_pk):
    user = get_user_model().objects.get(pk=accounts_pk)
    context = {
        'user':user,
    }
    return render(request, 'accounts/detail.html', context)


def login(request):
    if request.method == "POST":
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            auth_login(request, login_form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        login_form = AuthenticationForm()
    context = {
        'login_form':login_form,
    }
    return render(request,'accounts/login.html',context)

def logout(request):
    auth_logout(request)
    messages.warning(request, '로그아웃 하였습니다.')
    return redirect('articles:index')

@login_required
def update(request):
    if request.method == "POST":
        update_form = CustomUserChangeForm(request.POST, instance=request.user)
        if update_form.is_valid():
            update_form.save()
            return redirect('accounts:detail', request.user.pk)
    else:
        update_form = CustomUserChangeForm(instance=request.user)
    context = {
        'update_form':update_form,
    }
    return render(request, 'accounts/update.html', context)