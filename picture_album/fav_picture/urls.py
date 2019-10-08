from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/',views.add_fav,name='add_fav'),
    path('view/<int:pk>',views.view_fav,name='view_fav'),
]
