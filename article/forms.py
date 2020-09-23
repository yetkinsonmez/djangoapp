from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta: #Article ile ArticleForm'u bağlayarak çok kolay bir form oluşturduk
        model = Article 
        fields = ["title","content","article_image"]

