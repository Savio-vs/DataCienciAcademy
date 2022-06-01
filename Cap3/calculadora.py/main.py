
valor1=int(input('Digite o primeiro número:'))
sinal=input('Digite o sinal da operação:')
valor2=int(input('Digite o segundo valor:'))

if sinal =='+':
    resultado = valor1 + valor2
elif sinal =='-':
    resultado = valor1-valor2
elif sinal == '*':
    resultado = valor1*valor2
elif sinal =='/':
    resultado = valor1/valor2
elif sinal =='^':
    resultado = valor1**valor2
else:
    print ('Digite um sinal de operação valido.\nExemplo * , + , - , / , ^ .')
    exit()

print('resultado de %d %s %d é %d'%(valor1,sinal,valor2,resultado))
