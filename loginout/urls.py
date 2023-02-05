from re import template
from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'loginout'

urlpatterns = [
    
    path('login/', auth_views.LoginView.as_view(template_name='loginout/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]