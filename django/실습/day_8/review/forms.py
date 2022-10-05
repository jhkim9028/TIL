from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = '__all__'
        
        # fields = ['title', 'content'] 이런 식으로 원하는 것만 가능
