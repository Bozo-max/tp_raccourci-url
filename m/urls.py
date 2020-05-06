from django.urls import path
from . import views

urlpatterns = [
    path('index', views.home, name = "home"),
    path('add_url', views.add_url, name = 'add_url'),
    path('<str:code>', views.redirect_by_code, name = "redirect_by_code")
]
