from django.urls import path
from . import views
urlpatterns =[
    path("reg/", views.reg, name='registration'),
    path("login/", views.login, name='login')
]