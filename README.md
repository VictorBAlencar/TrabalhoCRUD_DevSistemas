# CRUD - Python

## INSTRUÇÕES DO TRABALHO

### Trabalho em Dupla - CRUD com SQLite

#### Objetivo: 
  Aplicar os conceitos de SQLite e funções CRUD para construir um sistema simples de gerenciamento de estoque ou inventário.

#### Descrição da Atividade:
  Cada dupla deve desenvolver um programa em Python que gerencie um pequeno estoque de produtos utilizando um banco de dados SQLite. O sistema deve permitir as seguintes operações:
  <ul>
      <li>Criar o banco de dados e a tabela produtos com os campos: </li><br>
      <li>id (chave primária, com auto incremento) </li><br>
      <li>nome (texto, único e obrigatório) </li><br>
      <li>quantidade (inteiro, obrigatório) </li><br>
      <li>preco (real, obrigatório) </li><br>
  </ul>

#### Implementar funções CRUD:
<ul>
  <li> Criar um novo produto no estoque. </li><br>
  <li> Listar todos os produtos disponíveis. </li><br>
  <li> Atualizar a quantidade e o preço de um produto existente. </li><br>
  <li> Deletar um produto pelo ID. </li><br>
  <li> Criar um menu interativo sem GUI onde o usuário pode escolher as opções acima. </li><br>
</ul>

#### Requisitos Técnicos
<ul>
  <li> O banco de dados deve ser criado automaticamente ao executar o programa. </li><br>
  <li> O código deve ser modularizado, com funções separadas para cada operação. </li><br>
  <li> O programa deve tratar erros, como tentativa de inserir um nome duplicado ou excluir um ID inexistente. </li><br>
  <li> O menu deve permitir que o usuário execute várias operações até decidir sair. </li><br>
</ul>

#### Critérios de Avaliação
<ul>
  <li> Funcionalidade: O código deve executar corretamente todas as operações CRUD. </li><br>
  <li> Organização: O código deve estar bem estruturado, com funções separadas. </li><br>
  <li> Tratamento de erros: O programa deve evitar falhas ao inserir dados duplicados ou inválidos. </li><br>
  <li> Interatividade: O menu deve ser amigável e permitir múltiplas operações. </li><br>
</ul>

#### Relatório da Atividade (entregas no moodle)
  Cada dupla deve entregar um relatório contendo:
  Código-fonte do programa (pasta zip - link do github ou colab ou google drive) <br>
