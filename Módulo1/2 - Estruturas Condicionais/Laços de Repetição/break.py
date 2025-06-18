#Break é utilizado para parar o looping

while True:
    numero = int(input("Informe um número: "))
    if numero == 10:
        break

    print(numero)

for numero in range(100):
    if numero == 13:
        break

    print(numero, end=" ")