#Criando um diocionário
#Dicionarios só aceitam valores imutaveis
#Dicionario é um conunto não-ordenado de pares chave:valor, onde as chaves são unicas em uma instancia do dicionario
#Dicionarios são delimitados por {}, e contem uma lista de pares chave:valor separada por virgula
         #chave   #valor      #chave #valor
pessoa = {"nome": "Matheus", "idade": 28}
pessoa = dict(nome= "Matheus", idade= 28)
pessoa["telefone"] = "1111-1111" #{"nome": "Matheus", "idade": 28, "telefone": "1111-1111"}

print(pessoa["nome"])
print(pessoa["idade"])
print(pessoa["telefone"])

#sobreescrevendo os dicionarios
pessoa["nome"] = "Militão"
pessoa["idade"] = 18
pessoa["telefone"] = "97013-2958"

print(pessoa["nome"])
print(pessoa["idade"])
print(pessoa["telefone"])

#Dicionarios aninhados
contato = {
    "teste@gmail.com": {"nome": "Milito", "idade": 18},
    "teste2@gmail.com": {"nome": "Silvestre", "idade": 38},
    "teste3@gmail.com": {"nome": "Latitude10", "idade": 28},
}

#acessando os dicionarios aninhados com a primeira chave
            #primeira chave   #chave dentro do dicionario
print(contato["teste2@gmail.com"]["nome"])
print(contato["teste@gmail.com"]["idade"])


#iterando dicionarios
for chave in contato:
    print(chave, contato[chave])

for chave, valor in contato.items():
    print(chave, valor)