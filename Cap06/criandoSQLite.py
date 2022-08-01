import sqlite3
import os 

os.remove ('escola.db') if os.path.exists('escola.db') else None # if escola.db existir na pasta delete
con = sqlite3.connect('escola.db')

print(type(con))

#fechar a conexão sempre
con.close()