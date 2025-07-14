email = str(input("Digite o email a ser validado: "))

if "@" in email:
    if "outlook.com" or "gmail.com" in email:
        print("Email validado com sucesso!")
    else:
        print("Faltam informações no email.")
else:
    print("Email inválido!")