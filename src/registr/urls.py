from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signupuser/', views.signupuser, name='signupuser'),
    path('login/', views.user_login, name='userlogin'),
    path('logout', views.logoutuser, name='logoutuser')

]