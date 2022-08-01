import sqlite3

con = sqlite3.connect('escola.db')
cur = con.cursor()

# sentença DML de seleção 
sql_select = 'select * from cursos'
#executar a sentença dentro do banco
cur.execute(sql_select)

#guardar os dados selecionados na variavel para serem usados.
dados = cur.fetchall()

#imprimir cada tupla de dados.
for linha in dados:
    print('Curso ID: %d, Título: %s, Categoria: %s'% linha)
#pode ser escrito também.
'''for linha in cur.fetchall():
    print('Curso ID: %d, Título: %s, Categoria: %s'% linha)  
'''
#fechar a conexão sempre
con.close()