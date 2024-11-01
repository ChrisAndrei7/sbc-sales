Feature: Gerenciamento de sales

  Scenario: Adicionar um novo Sale
    Given que eu tenho os detalhes do Sale
    When eu faço o cadastro de um Sale
    Then eu devo receber uma resposta com o código de status 200

  Scenario: Consultar um Sale
    When eu faço a consulta dos sales cadastros
    Then eu devo receber uma resposta com o código de status 200

  Scenario: Editar um Sale existente
    Given que eu tenho os detalhes atualizados do Sale
    When eu faço uma atualização de um Sale
    Then eu devo receber uma resposta com o código de status 200

  Scenario: Consultar um Sale pelo CPF
    When eu faço a consulta de um Sale pelo CPF
    Then eu devo receber uma resposta com o código de status 200

  Scenario: Consultar um Sale pela PLACA
    When eu faço a consulta de um Sale pelo PLACA
    Then eu devo receber uma resposta com o código de status 200