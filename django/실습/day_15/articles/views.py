from django.shortcuts import redirect, render
from .forms import CustomUserModelForm
from .models import Articles
# Create your views here.


def index(request):
    articles = Articles.objects.all()

    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def create(request):
    if request.method == "POST":
        form = CustomUserModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserModelForm()
    context = {
        'form':form,
    }
    return render(request, 'articles/create.html', context)

def detail(reqeust, pk):
    article = Articles.objects.get(pk=pk)
    context = {
        'article':article,
    }
    return render(reqeust, 'articles/detail.html',context)

def update(request, pk):
    article = Articles.objects.get(pk=pk)
    if request.method == "POST":
        form = CustomUserModelForm(request.POST, request.FILES,instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = CustomUserModelForm(instance=article)
    context = {
        'form':form,
    }
    return render(request, 'articles/update.html', context)

def delete(request, pk):
    Articles.objects.get(pk=pk).delete()
    return redirect('articles:index')