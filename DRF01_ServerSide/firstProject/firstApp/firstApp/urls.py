from django.urls import path
from firstApp import views

urlpatterns = [
    path('products/', views.get_products),
]