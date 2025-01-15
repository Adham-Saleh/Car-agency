from django.urls import path, include
from . import views

urlpatterns = [
    path('main/', views.carView, name='home'),
    path('create-car/', views.createCarView, name='create'),
    path('delete-car/<int:id>/', views.deleteCarView, name='delete'),
    path('car/<int:id>/', views.getCarView, name='singleCarPage'),
    path('car/<int:id>/edit/', views.updateCarView, name='editCar'),
    path('clients/', views.clientView, name='clients'),
    path('create-client/', views.createClientView, name='createClient'),
]