#Operadores de identidade (verificam se o que foi instanciado esta ocupando espaço na mesma memória)
#O operador de identidade é o Is
curso = "Bootcamp"
nome_bootcamp = curso
saldo, limite = 200, 200 

#São da mesma região de memória?
print(curso is nome_bootcamp) #true

#São da mesma região de memória?
print(curso is not nome_bootcamp) # false