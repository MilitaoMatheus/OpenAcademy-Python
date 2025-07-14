#Métodos de listas
lista = []

#Inserindo itens na lista
lista.append(1)
lista.append("teste")
lista.append([10, 20, 30])
print(lista)

#Apagando os itens da lista
lista.clear()
print(lista)

#Copiando uma lista (o que eu alterar na lista copia não vai afetar a lista original)
lista = [1, 'teste', [10, 20, 30]]
ls = lista.copy()

ls[0] = 120
print(ls)
print(lista)

#Contando quantas vzs um objeto aparece na lista
cores = ["Azul", "Verde", "Azul", "Azul", "Vermelho"]
print(cores.count("Azul")) #3
print(cores.count("Vermelho")) #1
print(cores.count("Verde")) #1

#Adicionando mais de um elemento ao mesmo tempo (aceita valores duplicados)
linguagens = ["Java", "Python", "C#"]
print(linguagens)
linguagens.extend(["js","C"])
print(linguagens)

#Encontrando o indice de um elemento
print(linguagens.index("Java")) #0
print(linguagens.index("js")) #3

#Retirando o ultimo elemento (oom e sem parametro)
linguagens.pop() #tira o C
linguagens.pop() #tira o js
linguagens.pop(0) #retira o Java
print(linguagens)

#Retirando elementos atraves do obeto em si
linguagens.remove("C#") #deixa somente o python
print(linguagens)

linguagens.extend(["js","C", "Java", "Python", "C#"])

print(linguagens)

#Invertendo a ordem da lista
linguagens.reverse()
print(linguagens)

#Orgaizando a exibião da lista (crescente, alfabética, etc) [.sort & .sorted]
linguagens.sort() #alfabética
print(linguagens)

linguagens.sort(reverse=True) #alfabética de trás pra frente
print(linguagens)

linguagens.sort(key=lambda x: len(x)) #por extensão da palavra 
print(linguagens)

linguagens.sort(key=lambda x: len(x), reverse=True) #por extensão da palavra (menor para maior)
print(linguagens)

#Verificndo a quantidade de elementos presente na lista (tamanho dela)
print(len(linguagens))