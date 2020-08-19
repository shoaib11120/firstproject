from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.http import HttpRequest

# region Login Form

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

# endregion

# region SignUP Form 

class signUPForm(forms.ModelForm):
    
    password=forms.CharField(widget=forms.PasswordInput,label="Password")
    confirm_password=forms.CharField(widget=forms.PasswordInput,label="Confirm Password")
   
    class Meta:
            model = User
            fields = ('username', 'first_name', 'email')

# endregion

# region Profile Edit Form

class userProfileEdit(forms.ModelForm):
    class Meta:
        model=User
        fields=('email','first_name','last_name')
        request = HttpRequest()
        widgets={
                   "email":forms.TextInput(attrs={'disabled':'true','class':'innerFormInput'}),
                   "first_name":forms.TextInput(attrs={'disabled':'true','class':'innerFormInput'}),
                   "last_name":forms.TextInput(attrs={'disabled':'true','class':'innerFormInput'}),
                } 

# endregion

# region Photo Edit

class userPhotoEdit(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('photo',)

# endregion


