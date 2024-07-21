from django.urls import path
from . import views

urlpatterns = [
    path('',views.loginPage,name = "login"),
    path('home/',views.home,name = "home page"),
    path('logout/',views.logoutPage,name = "logout"),
    path('register/',views.RegisterPage,name = "register"),
]