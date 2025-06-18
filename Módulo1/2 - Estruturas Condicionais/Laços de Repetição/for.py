#For -> utilizar quando saber quantas vezes o bloco de comando será executado
"""
texto = input("Digite uma palavra com vogal: ")
vogais = 'AEIOU'

for letra in texto:
    if letra.upper() in vogais:
        print(letra, end="")
else: 
    print("Executa no final do laço")
"""

#Função range() -> produz uma sequencia de numeros a partir de um inicio para um fim 
#Recebe 3 parâmetros -> stop, start (opcional) e step (opicional)
#É necessário passar um list para printar um range
print(list(range(0,10,2))) #Pulando de 2 em 2 
print(list(range(11))) #Passando o argumento de em que parte vai parar
print(list(range(2,10))) #Passanndo somente o inicio e fim 

#contagem
for number in range(0, 11):
    print(number, end=" ") #O end="" adiciona um espaço em branco, ou um caracter esolhido, ao fim de cada caracter/palavra

print()
#tabuada do 10
for numero in range(0, 101, 10):
    print(numero, end=" ")