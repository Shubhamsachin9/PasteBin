from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('paste/<int:pk>/edit/', views.paste_edit, name='paste_edit'),
    path('paste/<int:pk>/delete/', views.paste_delete, name='paste_delete'),
]
