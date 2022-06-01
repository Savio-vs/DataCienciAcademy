import pandas as pd
import os
"""open("diretorio",("r","w","a")) = Usada para abrir o arquivo
read() = Leitura do arquivo
write() = Gravação no arquivo
seek() = retorna para o início 
readlines() = Lê o arquivo linha a linha
for line in open("diretorio.txt"):
    print(line)
split() = separa levando com consideração o caractere informado
close() = fecha o arquivo
"""

"""arq1 = open("Cap04/arquivos/teste.txt","r")
print(arq1.read())
#numero de caracteres 
print(arq1.tell())
#posisão das coordenadas indicadas
print(arq1.seek(0,0)) 
#imprimi 10 caracteres apartir de onde estiver o cursor
print(arq1.read(10)) """

#abrir arquivo e adicionar um texto 
"""arq2 = open("Cap04/arquivos/teste.txt","a")
arq2.write("\nadicionando uma frase ao arquivo.")
arq2.close()
arq2 = open("Cap04/arquivos/teste.txt","r")
print(arq2.read())
# após finalizar qualquer ação dentro do arquivo fecheio.
arq2.close() 
arq2= open("Cap04/arquivos/teste.txt","w")
arq2.write("conteúdo do arquivo deletado!!!")
arq2.close()"""

"""file = pd.read_csv("Cap04/arquivos/dados.csv")
print(file.head())
"""

# MANIPULAÇÃO DE ARQUIVOS
"""with open ("Cap04/arquivos/dados.csv","r") as arquivo:
    conteudo = arquivo.read()

print(len(conteudo))
#print(conteudo) 

with open ("Cap04/arquivos/texto2.txt","w") as arquivo:
    arquivo.write(conteudo[:20])
    arquivo.write('\n')
    arquivo.write(conteudo[20:40])

with open("Cap04/arquivos/texto2.txt","r") as arquivo:
    texto = arquivo.read()

print(texto)"""