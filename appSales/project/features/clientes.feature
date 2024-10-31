Feature: Gerenciamento de clientes

  Scenario: Adicionar um novo Cliente
    Given que eu tenho os detalhes do Cliente
    When eu faço o cadastro de um Cliente
    Then eu devo receber uma resposta com o código de status 200

  Scenario: Consultar um Cliente
    When eu faço a consulta dos clientes cadastros
    Then eu devo receber uma resposta com o código de status 200

  Scenario: Editar um Cliente existente
    Given que eu tenho os detalhes atualizados do Cliente
    When eu faço uma atualização de um Cliente
    Then eu devo receber uma resposta com o código de status 200

  Scenario: Consultar um Cliente pelo CPF
    When eu faço a consulta de um Cliente pelo CPF
    Then eu devo receber uma resposta com o código de status 200