from django.urls import path
from . import views

urlpatterns = [
   
    path("login/", views.loginpage, name="loginpage"),
    path("register/", views.registerpage, name="registerpage"),
    path("logout/", views.userlogout, name="userlogout"),
    
 
]
