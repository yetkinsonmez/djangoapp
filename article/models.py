from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE) #on_delete=models.CASCADE sayesinde user silince tüm verileri de silinir
    title = models.CharField(max_length = 50) #,verbose_name = "blabla" yaparsan admin panelde ismi blabla olur
    content = RichTextField() #,verbose_name = "blabla" yaparsan admin panelde ismi blabla olur
    created_date = models.DateTimeField(auto_now_add=True)#auto_now_add=True sayesinde o anki tarihi oto alır
    article_image = models.FileField(upload_to='article_pics',blank = True,null=True,verbose_name="Add Image")
    
    def __str__(self):
        return self.title  #fonksiyonu sayesinde articles'da title a göre listelenir

    class Meta:
        ordering = ['-created_date']

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete= models.CASCADE, related_name="comments")
    comment_author = models.CharField(max_length = 120, verbose_name = "Author",null=True)
    comment_content = models.CharField(max_length = 180, verbose_name = "Content",null=True)
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.comment_content)
    
    class Meta:
        ordering = ['-comment_date']


