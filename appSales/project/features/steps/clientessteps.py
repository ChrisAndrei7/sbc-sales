from behave import given, when, then
import requests

BASE_URL = 'http://localhost:8004'

@given('que eu tenho os detalhes do Cliente')
def step_impl(context):
    context.cliente_data = {
        'NomeCliente': 'Paciente a',
        'cpf': '12871569088',
        'email': 'ba@ba.com.br',
        'senha': 'pass!paciente01@',
    }

@given('que eu tenho os detalhes atualizados do Cliente')
def step_impl(context):
    context.updated_cliente_data = {
        'NomeCliente': 'Paciente aZ',
        'cpf': '12871569088',
        'email': 'baZ@baZ.com.br',
        'senha': 'pass!paciente01@',
    }

@when('eu faço o cadastro de um Cliente')
def step_impl(context):
    context.response = requests.post(f"{BASE_URL}/sales/create", json=context.cliente_data)

@when('eu faço uma atualização de um Cliente')
def step_impl(context):
    context.response = requests.put(f"{BASE_URL}/sales/update/1", json=context.updated_cliente_data)

@when('eu faço a consulta dos sales cadastros')
def step_impl(context):
    context.response = requests.get(f"{BASE_URL}/sales")

@when('eu faço a consulta de um Cliente pelo CPF')
def step_impl(context):
    context.response = requests.get(f"{BASE_URL}/sales/readcpf/12871569088")

@when('eu faço a exclusão de um Cliente')
def step_impl(context):
    context.response = requests.delete(f"{BASE_URL}/sales/delete/1")

@then('eu devo receber uma resposta com o código de status 201')
def step_impl(context):
    assert context.response.status_code == 201

@then('eu devo receber uma resposta com o código de status 200')
def step_impl(context):
    assert context.response.status_code == 200
