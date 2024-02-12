import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

#cursor.execute('CREATE TABLE usuarios(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));') #Criar tabela com os campos
#cursor.execute('CREATE TABLE produtos(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')
#cursor.execute('CREATE TABLE gerentes(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')
#cursor.execute('ALTER TABLE usuarios RENAME TO usuario') #Alterar o nome da tabela
#cursor.execute('ALTER TABLE usuario ADD COLUMN telefone INT') #Alterar a tabela, adicionando uma coluna
#cursor.execute('ALTER TABLE usuario RENAME COLUMN telefoni TO telefone') #Alterar a tabela, renomeando uma coluna
#cursor.execute('DROP TABLE produtos') #Excluir tabela
#cursor.execute('INSERT INTO usuario(id, nome, endereco, email, telefone) VALUES (1, "Isadora", "França", "isa@gmail.com", 123456)') #Inserir dado na tabela
#cursor.execute('INSERT INTO usuario(id, nome, endereco, email, telefone) VALUES (2, "Maria", "São Paulo", "isa@gmail.com", 123456)')
#cursor.execute('INSERT INTO usuario(id, nome, endereco, email, telefone) VALUES (3, "José", "Curitiba", "isa@gmail.com", 123456)')
#cursor.execute('INSERT INTO usuario(id, nome, endereco, email, telefone) VALUES (4, "Márcia", "Salvador", "isa@gmail.com", 123456)')
#cursor.execute('DELETE FROM usuario where id=1') #Excluir dado da tabela

#cursor.execute('INSERT INTO gerentes(id, nome, endereco, email) VALUES (8, "Cynthia", "Inglaterra", "cy@gmail.com")')

#ORDER BY E DESC
#dados = cursor.execute('SELECT * FROM usuario ORDER BY nome DESC')

#LIMIT e DISTINCT
#dados = cursor.execute('SELECT DISTINCT * FROM usuario LIMIT 3')

#GROUP BY E HAVING
#dados = cursor.execute('SELECT nome FROM usuario GROUP BY nome HAVING id > 3')

#JOIN'S
#INNER JOIN - Pega todas as informações que tem correspondências em ambas as tabelas
dados = cursor.execute('SELECT * FROM usuario INNER JOIN gerentes ON usuario.id = gerentes.id')

#LEFT JOIN - Resultados da tabela à esquerda que correspondem à tabela da direta
#dados = cursor.execute('SELECT * FROM usuario LEFT JOIN gerentes ON usuario.id = gerentes.id')

#RIGHT JOIN - Preenche todos os dados à direita e trazer as correspondências na tabela à esquerda
#dados = cursor.execute('SELECT * FROM usuario RIGHT JOIN gerentes ON usuario.nome = gerentes.nome')

#FULL JOIN - Retorna todas as linhas das duas tabelas, comparando uma por uma
#dados = cursor.execute('SELECT * FROM usuario FULL JOIN gerentes ON usuario.nome = gerentes.nome')

#SUB-CONSULTAS - Consultas SQL que são alinhadas dentro da consulta principal. Utiliza o resultado de uma consulta como parte da condição de outra consulta
dados = cursor.execute('SELECT * FROM usuario WHERE nome IN (SELECT nome FROM gerentes)')
for usuario in dados:
    print(usuario)

#cursor.execute('UPDATE usuario SET endereco="Minas Gerais" WHERE nome="José"')

conexao.commit()
conexao.close