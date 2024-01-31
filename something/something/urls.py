from django.urls import path
from app_something import views

urlpatterns = [
    path('', views.index_page),
]
