from xml.etree.ElementTree import Comment
from django import forms
from django import forms
from .models import Articles, Comment

class ArticlesForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ['title','content','image','thumbnail']
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content',]
    