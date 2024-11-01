import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from entities.sales.salesmodels import Sale
from infrastructure.presenters.salesserializers import SaleSerializer


@api_view(['GET'])
def getData(request):
    sales = Sale.objects.all()
    serializer = SaleSerializer(sales, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getSale(request, pk):
    sales = Sale.objects.get(id=pk)
    serializer = SaleSerializer(sales, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getSaleCPF(request, cpf):
    sales = Sale.objects.get(cpf=cpf)
    serializer = SaleSerializer(sales, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def addSale(request):
    serializer = SaleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def updateSale(request, pk):
    sale = Sale.objects.get(id=pk)
    serializer = SaleSerializer(instance=sale, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteSale(request, pk):
    sale = Sale.objects.get(id=pk)
    sale.delete()
    return Response('Venda deletada com sucesso!')
