from tkinter.ttk import Widget
from .models import Post
from django import forms

class BlogPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author','category','sub_category','title','image','desc']
        widgets={
            'author':forms.Select(attrs={'class' :'form-control'}),
            'category':forms.Select(attrs={'class' :'form-control'}),
            'sub_category':forms.Select(attrs={'class' :'form-control'}),
            'title':forms.TextInput(attrs={'class' :'form-control'}),
            
            
            }