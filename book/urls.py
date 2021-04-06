"""BookProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import book_create,view_book,update_book,delete_book,home

urlpatterns = [
    path("creates",book_create, name="create"),
    path("view/<int:id>",view_book,name="view"),
    path("update/<int:id>",update_book, name="update"),
    path("delete/<int:id>",delete_book,name="delete"),
    path("",home,name="home")
]
