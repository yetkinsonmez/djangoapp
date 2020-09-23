from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "user"

urlpatterns = [
    path('register/',views.register,name = "register"),
    path('login/',views.login,name = "login"),
    path('logout/',views.logout,name = "logout"),
    path('profile/',views.profile,name = "profile"),
    path('dashboard/',views.dashboard,name = "dashboard"),
    path('editprofile/',views.editprofile,name = "editprofile"),
]