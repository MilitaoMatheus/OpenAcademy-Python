conta_normal = True
conta_universitaria = False

saldo = 2000
saque = 2100
chequeespecial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    elif saque <= (saldo + chequeespecial):
        print("Saue realizado com uso do cheque")
    else:
        print("Saque não realizado, saldo insuficiente")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    else:
        print("Saque não realizado, saldo insuficiente")