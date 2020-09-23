from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .forms import ArticleForm
from django.contrib import messages
from article.models import Article, Comment
from django.contrib.auth.decorators import login_required
# Create your views here.

def main(request): #renderları buraya yapıyorsun, requesti unutma
    return render(request,"main.html")  # 3. parametre olarak context adı altında bir dict girebilirsin. context = {"nums" : [10,20,30,40],"strs" : ["asdasd","aszx","xxax"]} \*/ main.html'de <ul>for num in nums <li>num</li></ul> veya str in strs şeklinde yazdırıyoruz

def articles(request):
    keyword = request.GET.get("keyword")

    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
        return render(request,"articles.html",{"articles" : articles})

    
    articles = Article.objects.all()
    context = {
        "articles":articles
    }
    return render(request,"articles.html",context)

def about(request):
    return render(request,"about.html")

def articlesid(request,id):
    return HttpResponse("ID: "+ str(id))

@login_required(login_url= "user:login")
def addArticle(request):
    form = ArticleForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        article = form.save(commit=False) #form bilgilerini al ama işleme

        article.author = request.user

        article.save()

        messages.success(request,"Article is successfully added.")
        return redirect("user:dashboard")

    return render(request,"addarticle.html",{"form":form})

@login_required(login_url= "user:login")
def detail(request,id):
    #article = Article.objects.filter(id = id).first()
    article = get_object_or_404(Article,id = id)

    comments = article.comments.all()

    return render(request,"detail.html",{"article":article,"comments":comments})

@login_required(login_url= "user:login")
def updateArticle(request,id):

    article = get_object_or_404(Article,id=id)

    form = ArticleForm(request.POST or None,request.FILES or None,instance=article)

    if form.is_valid():
        article = form.save(commit=False) #form bilgilerini al ama işleme

        article.author = request.user

        article.save()

        messages.success(request,"Article is successfully updated.")
        return redirect("user:dashboard")

    return render(request,"updatearticle.html",{"form":form})

@login_required(login_url= "user:login")
def deleteArticle(request,id):
    article = get_object_or_404(Article,id=id)

    article.delete()

    messages.success(request,"Article is successfully deleted")
    return redirect("user:dashboard")

@login_required(login_url= "user:login")
def addComment(request,id):
    article = get_object_or_404(Article,id=id)

    if request.method == "POST":
        comment_author = request.POST.get('name')
        comment_content = request.POST.get('body')

        newComment = Comment(comment_author = comment_author, comment_content = comment_content)

        newComment.article = article

        newComment.save()

    return redirect(reverse("article:detail", kwargs= {"id":id}))






