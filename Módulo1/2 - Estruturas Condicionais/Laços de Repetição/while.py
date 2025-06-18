#O comando Wile é utilizado para executar o bloco de codigo várias vezes (sem um numero exato de repetições)

opcao = 1

while opcao != 0:
    opcao = int(input("[1] sacar \n[2] extrato \n[0] sair \n: "))

    if opcao == 1:
        print("Sacando")
    elif opcao == 2:
        print("Exibindo extrato")
else:
    print("Obrigado por usar nosso sistema.")