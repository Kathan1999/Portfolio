from django.contrib import admin
from django.urls import path, include
from Home import views

urlpatterns = [
    path('', views.index, name="index"),
    path('blog/<slug:slug>/', views.blog, name="blog"),
]