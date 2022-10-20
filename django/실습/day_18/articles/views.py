from django.shortcuts import redirect, render
from .forms import ArticleForm, CommentForm
from .models import Article
from django.contrib import messages
# Create your views here.

def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles':articles,
    }
    return render(request,'articles/index.html',context)

def create(request):
    if request.method == "POST":
        create_form = ArticleForm(request.POST, request.FILES)
        if create_form.is_valid():
            article = create_form.save(commit=False)
            article.user = request.user
            article.save()
            messages.success(request, '글 작성이 완료되었습니다.')
            return redirect('articles:index')
    else:
        create_form = ArticleForm()
    context = {
        'create_form':create_form,
    }
    return render(request, 'articles/create.html', context)

def detail(request, articles_pk):
    article = Article.objects.get(pk=articles_pk)
    comment_form = CommentForm()
    user = article.user
    context = {
        'article':article,
        'comments':article.comment_set.all(),
        'comment_form':comment_form,
        'user':user,
    }
    return render(request, 'articles/detail.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        if request.method == "POST":
            update_form = ArticleForm(request.POST, instance=article)
            if update_form.is_valid():
                update_form.save()
                messages.success(request, '글이 수정되었습니다.')
                return redirect('articles:detail', article.pk)
        else:
            update_form = ArticleForm(instance=article)
        context = {
            'update_form':update_form,
        }
        return render(request, 'articles/update.html', context)
    else:
        messages.warning(request, '작성자만 수정할 수 있습니다.')
        return redirect('articles:detail', article.pk)

def delete(request,pk):
    Article.objects.get(pk=pk).delete()
    return redirect('articles:index')

def create_comment(request, comment_pk):
    article = Article.objects.get(pk=comment_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()
    return redirect('articles:detail', article.pk)