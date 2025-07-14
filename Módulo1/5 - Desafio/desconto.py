preco_orignal = float(input("Digite o preço do produto: "))
usar_desconto = str(input("Deseja usar cupom de desconto?(s/n): "))

if usar_desconto == "s":
    menu = """
        Cupons disponíveis: 
        [1] - DESCONTO10
        [2] - DESCONTO20
        [3] - SEMDESCONTO
        
        Qual cupom deseja usar?: """
    opcao = input(menu)

    if opcao == "1":
        produto_desconto = preco_orignal - (preco_orignal * (10/100))
        print(f"O valor do produto com desconto saiu por: R${produto_desconto:.2f}")
    
    elif opcao == "2":
        produto_desconto = preco_orignal - (preco_orignal * (20/100))
        print(f"O valor do produto com desconto saiu por: R${produto_desconto:.2f}")
    
    elif opcao == "3":
        print(f"Sem desconto. Valor do produto: R${preco_orignal:.2f}")
    
    else:
        print("Cupom não encontrado.")

elif usar_desconto == "n":
    print(f"Sem desconto. Valor do produto: R${preco_orignal:.2f}")
else:
    print(f"Digito inválido!")