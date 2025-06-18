#É necesssário uma identação para delimitar o inicio e o fim do bloco de código, aumentando a legibilidade do código
#Para definir um bloco de comando, o caracter : é utilizado. Exemplo -> if saldo > saque: ...

def sacar(self, valor: float): #inicio do bloco def
    if self.saldo >= valor: #inicio do bloco if
        self.saldo -= valor
    #fim do bloco if
#fim do bloco def

def saque(valor):
    saldo = 500
    if saldo >= valor:
        print("Valor sacado")
        print("Retire seu dinheiro na boca do caixa")
    print("Obrigado por ser nosso cliente!")

def depositar(valor):
    saldo = 500
    saldo += valor
    print(saldo)
depositar(100)