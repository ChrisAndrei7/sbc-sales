from rest_framework import serializers
from entities.clientes.clientesmodels import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'