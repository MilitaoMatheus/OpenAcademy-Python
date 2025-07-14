#Um conjunto não imprime valores duplicados, elimina registros duplicados (não garante a ordem)
set([1, 2, 3, 1, 3, ])# {1, 2, 3, 4}
set("abacaxi")# {"b", "a", "c", "x", "i"}
set(("palio", "gol", "celta", "palio")) #{"gol", "celta", "palio"}

#exemplo de set
linguagens = {"java", "python", "java"}

#Acessando os dados do set (necessário converter pra uma lista) 
num = {1, 2, 3, 4}
num = list(num)
print(num[0])

#iterando conjuntos
carros = {"palio", "gol", "celta"}
for carro in carros:
    print(carro)

#função enumerate
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")