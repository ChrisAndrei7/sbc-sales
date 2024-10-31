from django.urls import path
from application.usecases import clientesviews

urlpatterns = [
    path('', clientesviews.getData),
    path ('create', clientesviews.addCliente),
    path ('read/<str:pk>', clientesviews.getCliente),
    path ('readcpf/<str:cpf>', clientesviews.getClienteCPF),
    path ('update/<str:pk>', clientesviews.updateCliente),
    path ('delete/<str:pk>', clientesviews.deleteCliente),
]
