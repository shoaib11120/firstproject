from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('login/',views.LoginView,name='login'),
    path('profile/',views.profileView,name='profile'),
    path('logout/',views.logoutView,name='logout'),
    path('signup/',views.signupView,name='signup'),
]