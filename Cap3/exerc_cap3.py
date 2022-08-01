
import pandas as pd
#exer_2
"""lista_frutas = ['laranja','acerola','abacaxi','morango']
#cont=0
for item in lista_frutas:
    if item == 'morango':
        print('temos morango na lista')
        #caso queiramos que o codigo continui depois desse laço 
        #cont+=1
        #e retira o exit
        exit()
print('não temos morango.')"""
"""if cont == 0:
    print('não temos morango.')"""

#exer_3
"""tupla = (1,2,3,4)
resultado=[]
for i in range(len(tupla)):
    resultado.append(tupla[i] * 2)

print(resultado)"""

#exer_4
"""valores_pares = []
for i in range(100,150,2):
    valores_pares.append(i)

print(valores_pares)"""

#exer_5
"""temperatura = 40
while temperatura > 35:
    temperatura = int(input("Qual a temperatura atual?"))

print("condição de fim atingida.")"""

#exer_6
"""contador = 0 
while contador < 100:
    contador+=1
    if contador == 23:
        print("Número 23 encontrado.\nFim do programa.")
        break
    print(contador)"""

#Exercícios - Métodos e Funções
#01
"""def num_par():
    for i in range(0,21):
        if i %2 == 0:
            print("%s é um número par" %(i))

num_par()
print('FIM...')"""

#02
"""def maiuscula(s):
    print(s.upper())

maiuscula("passando uma string para maiuscula.")"""

#03
"""def add(lista):
    lista.append(10)
    lista.append(15)

lista= [14,4,8,9]
add(lista)
print('Lista final\n',lista)"""
    
#04
"""def func (valor , *valores):
    print('foi passado para a função apenas um valor -> ',valor)

    for i in valores:
        print('valor de entrada  -> %s '%(i))


func('passando um valor')

func('valor1','pasando mais de um valor',10,'ultimo valor',20,'testando')"""

#05
"""soma = lambda x,y: x+y
print(soma(100,15))
soma = lambda x,y: x**y
print(soma(4,2))"""

#07
"""Fah = lambda x: (x*(9/5)) + 32

Celsius = [39.2, 36.5, 37.3, 37.8,22.5]
Fahrenheit=[]
for i in Celsius:
    Fahrenheit.append(Fah(i)) 
print(Fahrenheit)"""

#08
"""dicionario = {'keys()':'->Retorna uma lista com todas as chaves do dicionário',
            'values()':'->Retorna uma lista com todos os valoresdo dicionário',
            'items()':'->Retorna uma lista com todos os pares chave/conteúdo',
            'fromkeys()':'->Retorna um novo dicionário cujas chaves são os elementos de lista e cujos valores são todos iguais a valor. Se valor não for especificado, o default é None.',
            'copy()':'->Retorna um outro dicionário com os mesmos pares',
            'clear()':'->Remove todos os elementos do dicionário',
            'get()':'->Obtém o conteúdo de chave. Não causa erro caso a chave não exista: retorna valor.',
            'update()':'->Atualiza um dicionário com os elementos de outro',
            'popitem()':'->Retorna e remove um par chave/valor aleatório do dicionário.',
            'pop()':'->Obtém o valor correspondente a chave e remove o par chave/valor do dicionário'}
ls_chave = dicionario.keys()
for i in ls_chave:
    print(dicionario.get(i))
#print(dicionario.values())"""

#09
file = pd.read_csv('Cap3/dados.csv')
print(file)



