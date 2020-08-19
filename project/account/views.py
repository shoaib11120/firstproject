from django.shortcuts import render,redirect
from .forms import LoginForm,signUPForm,userProfileEdit,userPhotoEdit
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User


# region LogIN View

def LoginView(request):
    
    if request.method == 'POST':
        form=LoginForm(request.POST)

        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(username=cd['username'],
                            password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('/')
                else:
                    return HttpResponse('Account Disabled')
            else:
                return HttpResponse('Account not valid')
    else:
        form=LoginForm()
    
    return render(request,
                'account/login.html',
                {'form':form,
                'css':'account/files/loginCss.html'})

# endregion

# region Profile View

def profileView(request):
    if request.method == 'POST':
        form = userProfileEdit(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
    else:
        form=userProfileEdit()
    return render(request,
                'account/profile.html',
                {'profileEdit':form,
                'css':'account/files/profileCss.html',
                'js':'account/files/profileJs.html'})
    
# endregion

# region LogOUT View 

def logoutView(request):
    logout(request)
    return redirect('/')

# endregion

# region Signup View

def signupView(request):
    if request.method == 'POST':
        form=signUPForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            if User.objects.filter(username = cd['username']).exists():
                return render(request,
                'account/signup.html',
                {'form':form,
                'mesg':'Username Taken',
                'css':'account/files/signupCss.html'})
            else:
                if User.objects.filter(email = cd['email']).exists():
                    return render(request,
                    'account/signup.html',
                     {'form':form,
                     'mesg':'Email Taken',
                     'css':'account/files/signupCss.html'})
                else:
                    if cd['password']==cd['confirm_password']:
                        user = User.objects.create_user(first_name=cd['first_name'],email=cd['email'],password=cd['password'],username=cd['username'])
                        return redirect('/account/login')
                    else:
                        return render(request,
                        'account/signup.html',
                        {'form':form,
                        'mesg':'Password didn\'t matched',
                        'css':'account/files/signupCss.html'})
                    
    else:
        form=signUPForm()
    return render(request,
                'account/signup.html',
                {'form':form,
                'css':'account/files/signupCss.html'})

# endregion


