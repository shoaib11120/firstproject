from django.urls import path
from account.api.views import registerView,loginView

app_name = 'account'


urlpatterns = [
    path('signup',
        registerView,
        name = 'apiSignup'),
    path('login',
        loginView,
        name = 'apiLogin'),
]