from django.contrib import admin

from .models import Article,Comment #models dosyası içindeki Article classını al
# Register your models here.

admin.site.register(Comment)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = ["title","author","created_date"]
    list_display_links = ["author","created_date"]

    search_fields = ["title"]

    list_filter = ["created_date"]
    class Meta: #ismi Meta olmak zorunda
        model = Article