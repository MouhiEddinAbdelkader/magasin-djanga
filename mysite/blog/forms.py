from .models import Post
from django import forms

class PostForm(forms.ModelForm):
   class Meta:
       model = Post
       fields = ['title','slug','author','content', 'status', 'image']