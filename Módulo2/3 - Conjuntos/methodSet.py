#Métodos do Set

#União
conjunto_a = {1, 2}
conjunto_b = {3, 4}
print(conjunto_a.union(conjunto_b)) #{1, 2, 3, 4}

#Operação de intersecção (partes iguais dos conjuntos)
conjunto_c = {1, 2, 3}
conjunto_d = {2, 3, 4}
print(conjunto_c.intersection(conjunto_d)) #{2, 3}

#Operação de diferença (onde esta em um, mas não no outro)
print(conjunto_c.difference(conjunto_d)) #{1}
print(conjunto_d.difference(conjunto_c)) #{4}

#Diferença simetrica (todos os elementos que não se interseccionam)
print(conjunto_c.symmetric_difference(conjunto_d)) #{1, 4}

#Metodo de um subconjunto presente em outro
conjunto_1 = {1, 2, 3}
conjunto_2 = {4, 1, 2, 5, 6, 3}
print(conjunto_1.issubset(conjunto_2)) #todos os valores do conjunto_1 está em conjunto_2? True
print(conjunto_2.issubset(conjunto_1)) #todos os valores do conjunto_2 está em conjunto_1? False

#Metodo contrário ao de cima
print(conjunto_1.issuperset(conjunto_2)) #todos os valores do conjunto_2 está em conjunto_1? False
print(conjunto_2.issuperset(conjunto_1)) #todos os valores do conjunto_1 está em conjunto_2? True

#Metodo de verificação se os elementos de um conjunto não estam presente em outro
a_conjunto = {1, 2, 3, 4, 5}
b_conjunto = {6, 7, 8, 9}
c_conjunto = {1, 0}
print(a_conjunto.isdisjoint(b_conjunto)) # A não está presente em B? True
print(a_conjunto.isdisjoint(c_conjunto)) # A não está presente em C? False

#Adicionando itens a um set
sorteio = {1, 23}
sorteio.add(25) #{1, 23, 25}
sorteio.add(42) #{1, 23, 25, 42}
sorteio.add(25) #{1, 23, 25, 42}
print(sorteio)
#Limpando um Set
sorteio.clear()
print(sorteio)

#Copiando uma set
teste = {1, 2}
print(sorteio) #{1, 2} 
sorteio.copy()
print(sorteio) #{1, 2}

#Discartando itens de um set
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
print(numeros) #{1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
numeros.discard(1)
numeros.discard(45)
print(numeros) #{0, 2, 3, 4, 5, 6, 7, 8, 9}

#retirando os primeiros valores 
num = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
print(num)
print(num.pop()) #0
print(num.pop()) #1
print(num.pop()) #2
print(num.pop()) #3

#Removedo um elemento especifico (se passar sem argumento, da erro)
num1 = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
num1.remove(0)
print(num1)

#Verificando o tamanho de um set
print(len(num1))

#verificando se algo esta presente em um set
num2 = {1, 2, 3, 4, 5, 6, 7, 8}
print(1 in num2) # true
print(10 in num2) # false