#Bootcamp Data Analytics - Exercícios Banco de Dados

#1. Crie uma tabela chamada "alunos" com os seguintes campos: id(inteiro), nome (texto), idade (inteiro) e curso (texto).

#Conexão ao banco de dados
import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()
cursor.execute('PRAGMA foreign_keys = 1') #Necessário para habilitar criação de foreign keys no sqlite

#Criação da tabela alunos
#cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100));')

#2. Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.

#Inserindo dados na tabela
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (1, "Maria", 20, "Engenharia")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (2, "José", 29, "Engenharia")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (3, "Paulo", 18, "Educação Física")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (4, "Natália", 36, "Nutrição")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (5, "Daniela", 25, "Medicina")')

#3. Consultas Básicas - Escreva consultas SQL para realizar as seguintes tarefas:
#a) Selecionar todos os registros da tabela "alunos".

#dados = cursor.execute('SELECT * FROM alunos')
#for alunos in dados:
#    print(alunos)

#b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
    
#dados = cursor.execute('SELECT nome, idade FROM alunos WHERE idade > 20')
#for alunos in dados:
#    print(alunos)

#c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.

#dados = cursor.execute('SELECT * FROM alunos WHERE curso = "Engenharia" ORDER BY nome')
#for alunos in dados:
#   print(alunos)

#d) Contar o número total de alunos na tabela

#dados = cursor.execute('SELECT COUNT(nome) FROM alunos ')
#for alunos in dados:
#   print(alunos)

#4. Atualização e Remoção
#a) Atualize a idade de um aluno específico na tabela.

#cursor.execute('UPDATE alunos SET idade = 28 WHERE nome = "Paulo"')

#Conferindo se a consulta deu certo
#dados = cursor.execute('SELECT * FROM alunos')
#for alunos in dados:
#   print(alunos)

#b) Remova um aluno pelo seu ID

#cursor.execute('DELETE FROM alunos where id=1')

#Conferindo se a consulta deu certo
#dados = cursor.execute('SELECT * FROM alunos')
#for alunos in dados:
#  print(alunos)

#5. Criar uma Tabela e Inserir Dados
#Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns registros de clientes na tabela.

#Criação da tabela
#cursor.execute('CREATE TABLE clientes(id integer PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), idade INT, saldo FLOAT);')

#Criação de registros
#cursor.execute('INSERT INTO clientes(nome, idade, saldo) VALUES ("Maria", 20, 4500)')
#cursor.execute('INSERT INTO clientes(nome, idade, saldo) VALUES ("José", 29, 5100)')
#cursor.execute('INSERT INTO clientes(nome, idade, saldo) VALUES ("Paulo", 18, 2800)')
#cursor.execute('INSERT INTO clientes(nome, idade, saldo) VALUES ("Natália", 36, 5600)')
#cursor.execute('INSERT INTO clientes(nome, idade, saldo) VALUES ("Daniela", 25, 6000)')

#6. Consultas e Funções Agregadas
#Escreva consultas SQL para realizar as seguintes tarefas:

#a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.

#dados = cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30')
#for clientes in dados:
#    print(clientes)

#b) Calcule o saldo médio dos clientes.

#dados = cursor.execute('SELECT AVG(saldo) FROM clientes')
#for clientes in dados:
#    print(clientes)

#c) Encontre o cliente com o saldo máximo.

#dados = cursor.execute('SELECT nome, MAX(saldo) FROM clientes')
#for clientes in dados:
#    print(clientes)

#d) Conte quantos clientes têm saldo acima de 1000.

#dados = cursor.execute('SELECT COUNT(nome) FROM clientes WHERE saldo > 1000')
#for clientes in dados:
#   print(clientes)

#7. Atualização e Remoção com Condições
#a) Atualize o saldo de um cliente específico.

#cursor.execute('UPDATE clientes SET saldo = 560 WHERE nome = "Paulo"')

#Conferindo se a consulta deu certo
#dados = cursor.execute('SELECT * FROM clientes')
#for clientes in dados:
#  print(clientes)

#b) Remova um cliente pelo seu ID.

#cursor.execute('DELETE FROM clientes where id=2')

#Conferindo se a consulta deu certo
#dados = cursor.execute('SELECT * FROM clientes')
#for clientes in dados:
#  print(clientes)

#8. Junção de Tabelas
#Crie uma segunda tabela chamada "compras" com os campos: id (chave primária), cliente_id (chave estrangeira referenciando o id da tabela "clientes"), 
#produto (texto) e valor (real). Insira algumas compras associadas a clientes existentes na tabela "clientes". Escreva uma consulta para exibir o nome do cliente, o produto e o
#valor de cada compra

#Criação da tabela
#cursor.execute('CREATE TABLE compras (id INTEGER PRIMARY KEY AUTOINCREMENT, cliente_id INTEGER NOT NULL, produto VARCHAR(100), valor FLOAT, CONSTRAINT compras_clientes_fk FOREIGN KEY (cliente_id) REFERENCES clientes(id));')

#Inserindo alguns registros na tabela
#cursor.execute('INSERT INTO compras(cliente_id, produto, valor) VALUES (3, "Smartphone", 3600)')
#cursor.execute('INSERT INTO compras(cliente_id, produto, valor) VALUES (5, "Smartphone", 4500)')
#cursor.execute('INSERT INTO compras(cliente_id, produto, valor) VALUES (1, "Smartphone", 4500)')
#cursor.execute('INSERT INTO compras(cliente_id, produto, valor) VALUES (5, "Smartphone", 8700)')
#cursor.execute('INSERT INTO compras(cliente_id, produto, valor) VALUES (4, "Smartphone", 7500)')

#Consulta para exibir nome do cliente, produto e o valor de cada compra
#dados = cursor.execute('SELECT nome, produto, valor FROM clientes INNER JOIN compras ON clientes.id = compras.cliente_id')