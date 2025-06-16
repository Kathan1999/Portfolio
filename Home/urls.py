from django.contrib import admin
from django.urls import path, include
from Home import views

urlpatterns = [
   path('', views.index, name="index"),
   path('post1', views.post1, name="post1"),
   path('post2', views.post2, name="post2"),
   path('post3', views.post3, name="post3"),
]
