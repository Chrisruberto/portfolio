from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_pago, name='create_pago'),
    path('edit/<int:pk>/', views.edit_pago, name='edit_pago'),
    path('delete/<int:pk>/', views.delete_pago, name='delete_pago'),
    path('list/', views.pago_list, name='pago_list'),
]