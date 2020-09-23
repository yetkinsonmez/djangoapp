from django import forms
from .models import Profile
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
    username = forms.CharField(min_length= 5, max_length=15,label = "Username")
    password = forms.CharField(min_length= 5, max_length=15,label = "Password",widget = forms.PasswordInput)
    confirm = forms.CharField(label = "Confirm password", widget = forms.PasswordInput)
    email = forms.EmailField(label = "Email")


    def clean(self):        
        cleaned_data = super().clean()
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")
        email = self.cleaned_data.get("email")

        if password and confirm and password != confirm:      
            raise forms.ValidationError("Passwords do not match")
        
        values = {
            "username" : username,
            "password" : password,
            "email" : email,

        }
        return values

class LoginForm(forms.Form):
    username = forms.CharField(label = "Username")
    password = forms.CharField(label = "Password",widget = forms.PasswordInput)

class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(min_length= 5, max_length=15,label = "Username")
    email = forms.EmailField(label = "Email")

    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']