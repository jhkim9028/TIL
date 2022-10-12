from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from review.forms import ReviewForm
from .models import Review

# Create your views here.

def home(request):
    return render(request,'review/home.html')

def index(request):
    reviews = Review.objects.order_by('-pk')
    context = {
        'reviews':reviews,
    }
    return render(request, 'review/index.html',context)

@login_required
def create(request):
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review_form.save()
            return redirect('review:index')
    else:
        review_form = ReviewForm()
        
    context = {
        'review_form':review_form,
    }
    return render(request, 'review/create.html',context)

def detail(request, pk):
    review = Review.objects.get(pk=pk)
    context = {
        'review':review,
    }
    return render(request, 'review/detail.html',context)

@login_required
def update(request, pk):
    
    review = Review.objects.get(pk=pk)
    
    if request.method == "POST":
        review_form = ReviewForm(request.POST, instance=review)
        if review_form.is_valid():
            review_form.save()
            return redirect('review:detail',review.pk)
    else:
        review_form = ReviewForm(instance=review)
        
    context = {
        'review_form':review_form,
    }
    return render(request, 'review/update.html',context)

def delete(request, pk):
    review = Review.objects.get(pk=pk)
    if request.method == "POST":
        review.delete()
        return redirect("review:index")
    else:
        return redirect('review:detail')
    
def search(request):
    search = request.GET.get('search')
    if Review.objects.filter(movie_name=search).exists():
        review = Review.objects.get(movie_name=search)
        return redirect('review:detail', review.pk)
    else:
        return render(request, 'review/not_find.html')