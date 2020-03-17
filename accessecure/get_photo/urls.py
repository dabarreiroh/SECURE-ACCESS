from django.urls import path,re_path
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    re_path(r'^photo/$', views.photo, name='camera'),
    re_path(r'^home/$', views.index, name='home'),
]