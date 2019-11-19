# 각 app의 urls.py 작성
from django.urls import path
from gpapp import views

urlpatterns = [
    path('insert', views.InsertFunc),
]