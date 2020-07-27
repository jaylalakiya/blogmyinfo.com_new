from django.contrib import admin
from django.urls import path, include
from blog.views import index, contact, about, post

urlpatterns = [
    path('', index),
    path('contact/', contact),
    path('about/', about),
    path('post/', post),
]
