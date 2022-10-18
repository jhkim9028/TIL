from django.shortcuts import redirect, render
from .forms import ArticlesForm, CommentForm
from .models import Articles, Comment
# Create your views here.


def index(request):
    articles = Articles.objects.all()

    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def create(request):
    if request.method == "POST":
        form = ArticlesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = ArticlesForm()
    context = {
        'form':form,
    }
    return render(request, 'articles/create.html', context)

def detail(reqeust, pk):
    article = Articles.objects.get(pk=pk)
    comment_form = CommentForm()
    context = {
        'article':article,
        'comments':article.comment_set.order_by('-pk'),
        'comment_form':comment_form,
    }
    return render(reqeust, 'articles/detail.html',context)

def update(request, pk):
    article = Articles.objects.get(pk=pk)
    if request.method == "POST":
        form = ArticlesForm(request.POST, request.FILES,instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticlesForm(instance=article)
    context = {
        'form':form,
    }
    return render(request, 'articles/update.html', context)

def delete(request, pk):
    Articles.objects.get(pk=pk).delete()
    return redirect('articles:index')

def comment_create(request, pk):
    article = Articles.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.save()
    return redirect('articles:detail', article.pk)

def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)