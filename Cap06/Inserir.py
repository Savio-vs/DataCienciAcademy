import sqlite3

#conectando ao banco (se ele não existir ele é criado)
con = sqlite3.connect('escola.db')
cur = con.cursor() #criando um cursor

'''# criando uma tabela com a linguagem SQL
sql_create = 'CREATE TABLE cursos'\
'( id int primary key, '\
'titulo varchar(40), '\
'categoria varchar(45) )'

cur.execute(sql_create) # escrever a tabela no BD'''

#criando sentença SQL para inserir registros 
sql_insert = 'insert into cursos values (?,?,?)'

#dados a serem inseridos na tabela
'''recset = [(1020,'Ciencia de dados','Data Science'),
(1030,'Big Data Fundametnos','Big data'),
(1040,'Python Fundamentos','Análise de dados')]'''

# percorrendo a lista recset com os dados, para poder executar 
# a sentença SQL com cada valor. 
'''for rec in recset :
    cur.execute(sql_insert,rec)

con.commit()'''

#inserir dados na tabela 

recset = [(1003,'arquitetura de computadores','ciencia da computação'),
(1004,'POO','Ciencia da Computação')]

for rec in recset :
    cur.execute(sql_insert,rec)
con.commit()

#fechar a conexão sempre
con.close()