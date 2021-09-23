from django.urls import path

from . import views

urlpatterns  = [
    path('', views.home, name='home'),
    path('books/', views.index, name='index'),
    path('authors/', views.authors, name='authors'),
    path('authors/new/', views.new_author, name='new_authors'),
]