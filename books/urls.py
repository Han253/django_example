from django.urls import path

from . import views

urlpatterns  = [
    path('', views.home, name='home'),
    path('books/', views.index, name='index'),
    path('authors/', views.authors, name='authors'),
    path('authors/new/', views.new_author, name='new_authors'),
    path('authors/update/<int:author_id>/', views.update_author, name='update_author'),
    path('authors/author/<int:author_id>/', views.detail_author, name='detail_author'),
    path('authors/delete/<int:author_id>/', views.delete_author, name='delete_author'),
]