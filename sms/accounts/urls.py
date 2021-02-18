from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/', views.signin, name="login"),
    path('', views.home, name="home"),
    path('logout/', views.signout, name="logout"),
]
