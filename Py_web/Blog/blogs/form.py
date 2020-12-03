from .models import BlogPost
from django import forms


class FormBlog(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text']
        labels = {'title': '标题', 'text': '正文'}
        widgets = {'text': forms.Textarea(attrs={'col': 400})}
    # title = forms.CharField(max_length=100)
    # text = forms.Textarea(attrs={'col': 80})
