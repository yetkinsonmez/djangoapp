from django.shortcuts import render,redirect
from .forms import RegisterForm, LoginForm, UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth import login as auth_login  #loginler karışıyor
from django.contrib.auth import logout as auth_logout
from article.models import Article
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    form = RegisterForm(request.POST or None) #post request olmadığında none'a gidip form = RegisterForm() halini alır ve işlevsiz kalır. sonra if'i geçip aşağıdaki contexten devam eder
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")
        
        newUser = User(username = username, email = email)
        newUser.set_password(password)
        newUser.save()
        auth_login(request,newUser)
        messages.success(request,"You successfully registered.")
        return redirect("main")
    
    context = {
        "form" : form
    }
    
    return render(request,"register.html",context)

def login(request):
    form = LoginForm(request.POST or None)

    context = {
        "form":form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username,password = password)

        if user is None:
            messages.info(request,"Username or Password is wrong. Try Again!")
            return render(request,"login.html",context)

        messages.success(request,"You successfully logined. Welcome!")
        auth_login(request,user)
        return redirect("main")

    return render(request,"login.html",context)

def logout(request):
    auth_logout(request)
    return redirect("main")

@login_required(login_url= "user:login")
def editprofile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, 
                                    request.FILES, 
                                    instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()                          
            messages.success(request,"Your account has been updated!")
            return redirect('user:profile')


    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        "u_form" : u_form,
        "p_form" : p_form
    }

    return render(request,"editprofile.html",context)

@login_required
def profile(request):
    return render(request,"profile.html")

@login_required(login_url= "user:login")
def dashboard(request):
    articles = Article.objects.filter(author = request.user) 
    context = {
        "articles":articles
    }
    return render(request,"dashboard.html",context)
