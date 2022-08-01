from unittest import result
from main import *

consulta1 = 'SELECT type, COUNT(*) as count from titles GROUP BY type'

resultado1 = pd.read_sql_query(consulta1,conn)

print(resultado1)

# criando uma coluna na pesquisa feita em consulta1.
resultado1['Percente'] = (resultado1['count'] / resultado1['count'].sum())*100
print(resultado1)

# Criar gráfico com apenas 3 categorias
# As 3 categorias com mais títulos. 
# dicionario vazio
others ={}
# criando uma categoria outros para colocar o restante dos títulos 
others['count'] = resultado1[resultado1['Percente']<5]['count'].sum()

others['percente'] = resultado1[resultado1['Percente']<5]['Percente'].sum()

others['Type'] = 'Others'

print(others)