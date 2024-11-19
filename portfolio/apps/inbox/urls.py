# apps/inbox/urls.py
from django.urls import path
from apps.inbox import views

urlpatterns = [
    path('', views.index, name='index'),  # Esto establece la ruta base de la app 'inbox'
]