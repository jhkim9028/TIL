from django.shortcuts import redirect, render
from .models import Review
from .forms import ReviewForm

# Create your views here.
def index(request):
    reviews = Review.objects.order_by('-pk')
    # Review.objects.all()
    context = {
        'reviews':reviews,
    }
    return render(request,'review/index.html', context)

# def new(request):
#     review_form = ReviewForm()
#     context = {
#         'review_form': review_form,
#     }
#     return render(request, 'review/new.html',context)

def detail(request, pk):
    review = Review.objects.get(pk=pk)
    context = {
        'review':review,
    }
    return render(request, 'review/detail.html', context)

def edit(request, pk_):
    
    review = Review.objects.get(pk=pk_)
    context = {
        'review':review,
    }
    return render(request, 'review/edit.html', context)

def create(request):
    # title_ = request.POST.get('title_')
    # content_ = request.POST.get('content_')
    
    # Review.objects.create(title=title_, content=content_)
    # 유효성 검사 및 DB 저장
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review_form.save()
            
            return redirect('review:index')
    else:
        review_form = ReviewForm()
        
    context = {
        'review_form': review_form,
    }
    return render(request, 'review/new.html',context=context)

def delete(request, pk_):
    Review.objects.get(pk=pk_).delete()
    return redirect('review:index')

def update(request, pk):
    # review = Review.objects.get(pk=pk)
    
    # title = request.GET.get('title')
    # content = request.GET.get('content')
    
    # review.title = title
    # review.content = content
    
    # review.save()
    review = Review.objects.get(pk=pk)
    if request.method == 'POST':
        review_form = ReviewForm(request.POST, instance=review)
        if review_form.is_valid():
            review_form.save()
            return redirect('review:detail', review.pk)
    else:
        review_form = ReviewForm(instance=review)
        
    context = {
        'review_form': review_form,
    }
    return render(request, 'review/edit.html',context)