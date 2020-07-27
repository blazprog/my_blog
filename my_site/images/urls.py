from django.urls import path
from . import views

urlpatterns = [
    path('', views.image_list, name='image_list'),
    path('image/<int:pk>/', views.image_detail, name='image_detail'),
    path('previous/<int:pk>/', views.image_previous, name='image_previous'),
    path('next/<int:pk>/', views.image_next, name='image_next'),
]
