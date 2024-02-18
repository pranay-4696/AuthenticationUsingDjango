from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.home,name="home"),
    
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('signout/',views.signout,name='signout'),
    path('activate/<str:uidb64>/<str:token>/', views.activate, name='activate'),
    path('login/', auth_views.LoginView.as_view(template_name='authentication/signin.html'), name='login'),
    path('signout/', views.signout, name='signout'),

]