from django import forms
from django import forms
from .models import Articles

class CustomUserModelForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ['title','content','image','thumbnail']