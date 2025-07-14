#A tupla é imutavel, não se altera
#A tupla é feita por () e ,

frutas = ("laranja", "pera", "uva",)
letras = tuple("python")
numeros = tuple([1, 2, 3, 4])

print(frutas[0]) #laranja
print(numeros[-1]) #4
print(letras[4]) #o

matriz = (
    (1, "a", 2),
    (3, 4, "b"),
    ("c", 5, 6),
)

print(matriz[0]) #(1, "a", 2),
#O primeiro colchetes indica a linha, e o segundo colchetes indica a posição
print(matriz[0][0]) #1
print(matriz[0][-1]) #2
print(matriz[-1][-3]) #c

#Fatiamento de listas
         # 0    1    2    3    4    5
python = ("p", "y", "t", "h", "o", "n")

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
