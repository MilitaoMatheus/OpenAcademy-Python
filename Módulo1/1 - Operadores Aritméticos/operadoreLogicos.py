saldo = 1000
saque = 200
limite = 100

#pra ter retorno END verdadeiro é necessário ambos os lados serem verdadeiros
print(saldo >= saldo and saque <= limite) #false

#pra ter retorno OR verdadeiro é necessário que um dos lados sejam verdadeiros
print(saldo >= saldo or saque <= limite) #true

#o NOT serve como negação de um bool (verdadeiro vira falso e falso vira verdadeiero)
print(not 100 > 20) #false
print(not 100 < 20) #true