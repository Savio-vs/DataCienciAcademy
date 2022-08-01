class Pessoa:
    def __init__(self,nome,cidade,telefone,email) -> None:
        self.nome = nome
        self.cidade = cidade.upper()
        self.telefone = telefone
        self.email = email
    def __str__(self) :         #retorna com print
        return '%s é um objeto Pessoa.' %(self.nome)
    
    def __cmp__(self,other):  #vale todas as comparações
        return self.cidade == self.cidade

pes1 =  Pessoa('João Paulo','Fortaleza','85981799202','joaopaulo@gmail.com')

pes2 = Pessoa('Ana Maria','Fortaleza','85999111548','maria@gmail.com')

print(pes1.cidade)
print(pes2.cidade)

if (pes1 == pes2) == 0:
    print('%s e %s moram em %s' %(pes1.nome,pes2.nome,pes1.cidade))
else:
    print('%s e %s moram em cidades diferentes!'%(pes1.nome,pes2.nome)) 



