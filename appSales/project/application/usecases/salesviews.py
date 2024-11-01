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

@api_view(['GET'])
def getSalePLACA(request, placa):
    sales = Sale.objects.get(placa=placa)
    serializer = SaleSerializer(sales, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def addSale(request):
    # Obtém a lista de CPFs de clientes do MS Clientes
    clientes_response = requests.get('http://clientes:8004/clientes')
    if clientes_response.status_code != 200:
        return Response({"erro": "Erro ao conectar com o serviço de clientes"}, status=500)

    try:
        clientes = clientes_response.json()
        clientes_cpf = [cliente['cpf'] for cliente in clientes]
    except ValueError:
        return Response({"erro": "Erro ao processar a resposta de clientes"}, status=500)

    # Verifica se o CPF do cliente existe no MS Clientes
    cpf_cliente = request.data.get('cpf')
    if cpf_cliente not in clientes_cpf:
        return Response({"erro": "Cliente com o CPF fornecido não encontrado"}, status=400)

    # Prossegue com a criação da venda se o cliente existir
    serializer = SaleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=400)

@api_view(['GET'])
def getClientes(request):
    # Consultando MS de clientes para obter a lista de médicos cadastrados
    clientes_response = requests.get('http://clientes:8004/clientes')

    if clientes_response.status_code != 200:
        return Response({"erro": "Erro ao conectar com o serviço de clientes"}, status=500)

    try:
        clientes = clientes_response.json()
    except ValueError:
        return Response({"erro": "Erro ao processar a resposta de clientes"}, status=500)

    # Filtrar médicos disponíveis
    clientes_disponiveis = [cliente['cpf'] for cliente in clientes]

    return Response({'clientes_disponiveis': clientes_disponiveis})


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
