#01 
'''valores = [2,3,4]
lista = list(map((lambda x: x**3), valores))
print(lista)'''

#02
'''frase = 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil'.split()
def at2(w) :
    return [w.upper(),w.lower(),len(w)]
        
for i in map (at2, frase):
    print(i)'''

#03
'''matrix = [[1, 2],[3,4],[5,6],[7,8]]
matrixT = [[],[]]
'''

'''for i in range (len(matrix[0])):
    lst = [x[i] for x in matrix]
    for j in lst:
        matrixT[i].append(j)

print(matrixT)'''

'''
for i in range (len(matrix[0])):
    lista = list(map(lambda m: m[i],matrix))
    for j in lista:
        matrixT[i].append(j)
'''

#04
'''
def quadrado (n):
    return  n**2

def cubo(n):
    return n**3
lista = [0,1,2,3,4]
l1=[]
l2=[]
for i in lista:
    l1.append (quadrado (i))
    l2.append(cubo(i))
print('Numeros ao quadrado ',l1,'\nNumeros ao cubo ',l2)
'''

#05
'''def eleve (a,b):
    return a**b

listaA = [2, 3, 4]
listaB = [10, 11, 12]
listaC=[]
for i in range(len(listaA)):
    listaC.append (eleve(listaA[i],listaB[i]))

print (listaC)'''

#06
'''def negativo(n):
    if n <0:
        return n
lista=[]
for i in range(-5,5):
    lista.append(i)

neg=list(filter(negativo,lista))
print (neg)'''

#07
'''a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8]
c=[]
for i in b:
    c+=(list(filter(lambda x: x==i,a)))
print (c)'''

#08
