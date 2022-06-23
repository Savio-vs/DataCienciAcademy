#01 
'''valores = [2,3,4]
lista = map((lambda x: x**3), valores)
print(list(lista))'''

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
