#O continue é uma variação do brea, e é utilizado para contornar algo do looping

#Mostrando os números impares
print("Ímpares: ")
for numero in range(11):
    if numero % 2 == 0:
        continue
    print(numero, end=" ")

print()

print("Pares: ")
#Mostrando os números pares
for numero in range(11):
    if numero % 2 != 0:
        continue
    print(numero, end=" ")
