from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('article/<int:pk>/', views.post_detail, name='post_detail'),
    path('article/<int:pk>/edit', views.post_edit, name='post_edit'),
    path('article/<int:pk>/edit_comment', views.comment_edit, name='comment_edit'),
]

