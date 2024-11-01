from behave import given, when, then
import requests

BASE_URL = 'http://localhost:8002'

@given('que eu tenho os detalhes do Sale')
def step_impl(context):
    context.sale_data = {
        'NomeCliente': 'Gabriel Silva',
        'cpf': '94827383810',
        'placa': 'KHM-1C11',
        'veiculo': 'Opala',
        'dataVenda': '14-10-2024',
        'status': 'Aguardando pagamento',
    }

@given('que eu tenho os detalhes atualizados do Sale')
def step_impl(context):
    context.updated_sale_data = {
        'NomeCliente': 'Gabriel Silva',
        'cpf': '94827383810',
        'placa': 'KHM-1C11',
        'veiculo': 'Opala',
        'dataVenda': '14-10-2024',
        'status': 'Finalizada',
    }

@when('eu faço o cadastro de um Sale')
def step_impl(context):
    context.response = requests.post(f"{BASE_URL}/sales/create", json=context.sale_data)

@when('eu faço uma atualização de um Sale')
def step_impl(context):
    context.response = requests.put(f"{BASE_URL}/sales/update/1", json=context.updated_sale_data)

@when('eu faço a consulta dos sales cadastros')
def step_impl(context):
    context.response = requests.get(f"{BASE_URL}/sales")

@when('eu faço a consulta de um Sale pelo CPF')
def step_impl(context):
    context.response = requests.get(f"{BASE_URL}/sales/readcpf/94827383810")

@when('eu faço a consulta de um Sale pelo PLACA')
def step_impl(context):
    context.response = requests.get(f"{BASE_URL}/sales/readplaca/KHM-1C11")

@when('eu faço a exclusão de um Sale')
def step_impl(context):
    context.response = requests.delete(f"{BASE_URL}/sales/delete/1")

@then('eu devo receber uma resposta com o código de status 201')
def step_impl(context):
    assert context.response.status_code == 201

@then('eu devo receber uma resposta com o código de status 200')
def step_impl(context):
    assert context.response.status_code == 200
