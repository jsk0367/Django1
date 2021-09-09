from django.contrib import admin
from django.urls import path
from . import views

app_name = 'noticeboard'
urlpatterns =[
    path('', views.index, name='index'),
    path('write/', views.write_article, name='write_article'),
    path('add/', views.add_article, name='add_article'),
    path('<int:article_id>/', views.view_article, name='view'),
    path('update/<int:article_id>/', views.update_article, name='update'),
    path('delete/<int:article_id>/', views.delete_article, name='delete'),
]