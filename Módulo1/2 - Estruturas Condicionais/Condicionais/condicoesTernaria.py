#Condição de uma única linha
#É composto por três partes: retorno (caso verdadeiro), expressão logica, retorno (caso falso)

saldo = 2000
saque = 500
status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao realizar o saque")