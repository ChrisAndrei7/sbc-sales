from django.urls import path
from application.usecases import salesviews

urlpatterns = [
    path('', salesviews.getData),
    path('create', salesviews.addSale),
    path('read/<str:pk>', salesviews.getSale),
    path('readcpf/<str:cpf>', salesviews.getSaleCPF),
    path('update/<str:pk>', salesviews.updateSale),
    path('delete/<str:pk>', salesviews.deleteSale),
]