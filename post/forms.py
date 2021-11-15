from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('category','title', 'text')
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'})
        }

        labels = {
            'category': '카테고리',
            'title': '제목',
            'text': '내용'
        }

    #title = forms.CharField(error_messages={'required': '제목을 입력하세요.'}, max_length=100, label="제목")
    #text = forms.CharField(error_messages={'required': '내용을 입력하세요.'}, widget=forms.Textarea, label="내용")