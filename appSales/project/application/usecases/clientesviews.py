import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from entities.clientes.clientesmodels import Cliente
from infrastructure.presenters.clientesserializers import ClienteSerializer


@api_view(['GET'])
def getData(request):
    clientes = Cliente.objects.all()
    serializer = ClienteSerializer(clientes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getCliente(request, pk):
    clientes = Cliente.objects.get(id=pk)
    serializer = ClienteSerializer(clientes, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getClienteCPF(request, cpf):
    clientes = Cliente.objects.get(cpf=cpf)
    serializer = ClienteSerializer(clientes, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def addCliente(request):
    serializer = ClienteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def updateCliente(request, pk):
    cliente = Cliente.objects.get(id=pk)
    serializer = ClienteSerializer(instance=cliente, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteCliente(request, pk):
    cliente = Cliente.objects.get(id=pk)
    cliente.delete()
    return Response('Cliente deletado com sucesso!')
