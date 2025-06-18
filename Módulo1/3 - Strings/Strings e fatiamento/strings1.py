#Manipulado Strings
#O dado String possui varios métodos
nome = "MaThEuS"
print(nome.upper()) #Passando a string para maiúsculo
print(nome.lower()) #Passando a string para minúsculo
print(nome.title()) #Passando a string para o estilo de título

print()

#Eliminando espaços em branco
sobrenome  = "  Silva  1  "
print(sobrenome)
print(sobrenome.strip()) #Apagando todos os espaçoes em branco após o fim da palavra
print(sobrenome.lstrip()) #Apagando todos os espaos em branco da direita
print(sobrenome.rstrip()) #Apagando todos os espaos em branco da esquerda

print()

#Centralização e junção
curso = "python"

#Método center -> .center(numero de caracteres que vai utilizar, caracter escolhido)
print(curso.center(10, "#"))
print(curso.center(12, "-"))

#Junção de caracteres entre as letras
#Método join passa letra por letra adicionando o caracer escolhido -> "caracter a ser inserido".join(variavel string)
print(".".join(curso))