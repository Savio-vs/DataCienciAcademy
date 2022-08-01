import re 
import time 
import sqlite3
import pycountry
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import cm
from sklearn.feature_extraction.text import CountVectorizer


conn = sqlite3.connect('imdb.db')       #conectando ao banco de dados

tabelas = pd.read_sql_query('SELECT NAME as "Table_Name" From sqlite_master where type = "table" ',conn)
#print(tabelas)

# tabelas é um data frame 
# vamos converter o dataframe em uma lista
tabelas = tabelas["Table_Name"].values.tolist()

# para cada tabela dentro de tabelas 
# será impresso os detalhes de cada uma.
'''for tabela in tabelas:
    consulta = "PRAGMA TABLE_INFO({})".format(tabela)
    resultado = pd.read_sql_query(consulta,conn)
    print("Esquema da tabela:",tabela)
    print(resultado)
    print("-"*100)
    print("\n")'''


