menu = """
Olá. Qual a opção desejada?

[1] - Depositar
[2] - Sacar
[3] - Ver Extrato
[4] - Sair

"""

saldo = 0
limite = 500
extrato = ""
qtd_saque = 0
LIMITE_SAQUE = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        deposito = float(input("Digite o valor a ser depositado: "))
        if deposito < 0:
            print("Digite valores maior que 0")
        else:
            saldo += deposito
            print(f"Deposito realizado com sucesso. Seu saldo é de {saldo}")
            extrato += f"Depósito de R${deposito:.2f}\n"
    
    elif opcao == "2":
        sacar = float(input("Digite o valor a ser sacado: "))
        if qtd_saque < LIMITE_SAQUE:
            if sacar > saldo or sacar > limite:
                print("Não foi possível sacar. Revise os valores do saque!")
            elif sacar < 0:
                print("Digite valores maior que 0")
            else:
                saldo -= sacar
                print(f"Saque realizado com suceso. Seu saldo é de: {saldo}")
                extrato += f"Saque de R${sacar:.2f}\n"
        else:
            print("Limite de saque diário atingido. Tente novamente amanhã.")
        qtd_saque += 1

    elif opcao == "3":
        if extrato != "":
            print(f"{"-" * 4} EXTRATOS {"-" * 3}")
            print(extrato)
        else:
            print(f"{"-" * 4} EXTRATOS {"-" * 3}")
            print("Nenhum extrato a ser exibido")
    
    elif opcao == "4":
        print("Obrigado por utilizar nosso sistema.")
        break

    else:
        print("Opção inválida!")