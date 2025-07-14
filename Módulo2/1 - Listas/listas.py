#Tudo em python é objeto
#Ums lista pode armazenar varios tipos de dados em si
#Exemplo

frutas = ["Maçã", "Banana", "Uva"]
print(frutas)

frutas = []
print(frutas)

#Coloca uma lista onde cada caracter é um elemento
letras = list("Python")
print(letras)

numeros = list(range(10))
print(numeros)

carro = ["Ferrari", "F8", 1000000, 2025, 2900, "São Paulo", True]
print(carro)

#Acesso direto (método de acessar um indice dentro de uma lista)
frutas = ["Maçã", "Banana", "Uva"]
print(frutas[1])
#Contagem com indices negativos pegam de trás pra frente
print(frutas[-1])
print(frutas[-2])

#Lista aninhada -> recebe mais de um tipo de dado (utilizado para a criação de matrizes)
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

#O primeiro colchetes indica a linha, e o segundo colchetes indica a posição
print(matriz[0]) #[1, "a", 2]
print(matriz[0][0]) #1
print(matriz[1][-1 ]) #4
print(matriz[-1][-1 ]) #c

#Fatiamento de listas
         # 0    1    2    3    4    5
python = ["p", "y", "t", "h", "o", "n"]

#passando a contagem inicial (a partir de X pra frente)
print(python[2:]) #["t", "h", "o", "n"]

#passando o final (de X pra tras)
print(python[:2]) #["p", "y"]

#passando o inicio e o fim (a partir de X até Y)
print(python[1:3]) #["y", "t"]

#passando o inicio e o fim com step (comece a partir de X até Y, pulando de Z em Z)
print(python[0:3:2]) #["p", "t"]

#Imprime a lista completa
print(python[::]) #["p", "y", "t", "h", "o", "n"]

#Imprime a lista de maneira espelhada
print(python[::-1]) #["n", "o", "h", "t", "y", "p"]



#Iterar listas
carros = ["gol", "celta", "focus"]
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")


#Compreensão de listas (criar uma lista com base em uma já existente ou criar uma nova lista com modificação)
num = [1, 30, 21, 2, 9, 65, 34]

#pegando numeros pares
pares = [numero for numero in num if numero % 2 == 0]
print(pares)

quadrado = [numero ** 2 for numero in num]
print(quadrado)