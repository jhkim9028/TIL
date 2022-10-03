from django.shortcuts import render, redirect
from .models import Review

# Create your views here.
def index(request):
    reviews = Review.objects.all()
    
    context = {
        'reviews':reviews,
    }
    return render(request,'review/index.html',context)

def new(request):
    return render(request, 'review/new.html')

def detail(request, pk_):
    review = Review.objects.get(pk=pk_)
    
    context = {
        'review': review,
    }
    return render(request,'review/detail.html',context)

def edit(request, pk__):
    review = Review.objects.get(pk=pk__)
    context = {
        'review':review,
    }
    return render(request,'review/edit.html',context)

def create(request):
    title = request.GET.get('title_')
    content = request.GET.get('content_')
    
    Review.objects.create(title=title, content=content)    
    return redirect('review:index')

def delete(request, pk):
    review = Review.objects.get(pk=pk)
    review.delete()
    
    return redirect('review:index')

def update(request, pk___):
    review = Review.objects.get(pk=pk___)
    
    title_ = request.GET.get('title_')
    content_ = request.GET.get('content_')
    
    review.title = title_
    review.content = content_
    
    review.save()
    return redirect('review:detail', review.pk)