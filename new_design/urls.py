from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home") ,
    # path('connect/user', views.user_connect) ,
]