from django.db import models

# Create your models here.

class Cliente(models.Model):
    NomeCliente = models.CharField(max_length=250)
    cpf = models.CharField(max_length=15)
    placa = models.CharField(max_length=250)
    veiculo = models.CharField(max_length=250)
    dataVenda = models.CharField(max_length=250)
    status = models.CharField(max_length=250)
