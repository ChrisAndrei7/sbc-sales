<h1 align="center"> SubCars - Sistema para revenda de carros </h1>
Bem-vindo ao Sistema para revenda de carros da SubCars! Este projeto está em desenvolvimento como atividade para a FIAP, curso Software Architecture.	
<br/>
<b>Neste repositório, temos o microsserviço de cadastro das vendas</b>

# :computer: Endpoint base da aplicação
http://localhost:8002/
<br/>
<br/>

# :hammer: Subida da aplicação
### Subida completa da aplicação via docker:

#### - Subida no docker:
1. Entre no diretório do projeto: `cd appSales`
2. Efetue a criação/subida do banco de dados: `docker compose up -d dbSales`
3. Efetue a criação da aplicação: `docker compose build`                                                                                                                                                                                                                                                     
      <b>Nota Importante:
      Ao realizar a primeira inicialização, ocasionalmente pode ocorrer o erro "No installed app with label 'sales'". Como solução temporária, sugerimos a seguinte abordagem: caso o erro mencionado ocorra na primeira subida, modifique o arquivo "django.sh" na linha       3, substituindo "sales" por "application" e efetue novamente o passo 3 antes de seguir para o passo 4.</b>
4. Efetue a subida da aplicação: `docker compose up`
<br/>
  
# :arrow_forward: Uso 
Abaixo, fluxos principais com processo e endpoint deste microsserviço. Para maior detalhe dos campos, temos no projeto(Na pasta appClientes/Documentos) o arquivo do Postman com a collection estruturando todos as APIs com descrição e valores a serem informados no json.

1 - Criar o cadastro de uma venda: http://localhost:8002/sales/create

2 - Consultar vendas cadastradas: http://localhost:8002/sales/

3 - Atualizar cadastro de uma venda: http://localhost:8002/sales/update/{id_da_venda}

4 - Deletar o cadastro de uma venda: http://localhost:8002/sales/delete/{id_da_venda}

# :page_with_curl: Collection
Disponibilizamos uma collection do postman para ajudar na utilização, contendo todas as APIs deste microserviço e com os campos necessários para preenchimento, <b>localizado na pasta appSales/Documentos com nome "sbc-sales.postman_collection".</b>

# :page_with_curl: Requisito de Negócios
Criamos um documento abordando o requisito de Negócios, <b>localizado na pasta appSales/Documentos com nome "Requisitos de Negocios - SubCars".</b>

# :test_tube: Testes
Para executar os testes, localizados dentro da pasta "feature", deve ser processado o comando behave abaixo após aplicação estar no ar.
<br/>
OBS: BDD está dentro do arquivo "clientes.feature"

#### behave appSales/project/features/sales.feature

# Evidência dos testes:

![sbc-sales_test](https://github.com/user-attachments/assets/447dc9c5-d23e-49c2-aec9-ed485079981d)
