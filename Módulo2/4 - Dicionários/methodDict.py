#clear (apaga o dicionario)
contato = {
    "teste@gmail.com": {"nome": "Milito", "idade": 18},
    "teste2@gmail.com": {"nome": "Silvestre", "idade": 38},
    "teste3@gmail.com": {"nome": "Latitude10", "idade": 28},
}
contato.clear()
print(contato)

#Método cópia
contatos = {
    "teste@gmail.com": {"nome": "Milito", "idade": 18},
    "teste2@gmail.com": {"nome": "Silvestre", "idade": 38},
    "teste3@gmail.com": {"nome": "Latitude10", "idade": 28},
}
copia = contatos.copy()
copia["teste@gmail.com"] = {"nome": "Math"}
print(contatos)
print(copia)

#Frokeys (cria as chaves para você, com ou sem valor padrao)
print(dict.fromkeys(["nome", "telefone"]))
print(dict.fromkeys(["nome", "telefone"], "vazio"))

#Get -> acessando o dicionario
contato1 = {
    "teste@gmail.com": {"nome": "Milito", "idade": 18},
}
# print(contato1["chave"]) #retorna um erro
print(contato1.get("chave", {})) # retorna {}
print(contato1.get("chave")) #retorna none
print(contato1.get("teste@gmail.com", {})) #retorna a info padrão

#items (retorna uma lista de tuplas)
print(contatos.items())

#keys(retorna uma lista com as chaves do cicionario)
novo_Dict = {"a": 100, "b": 10, "c": "oi"}
print(novo_Dict.keys())

#pop (excluindo a chave)
contato2 = {
    "teste@gmail.com": {"nome": "Milito", "idade": 18},
}
print(contato2)
print(contato2.pop("teste@gmail.com"))
print(contato2.pop("teste@gmail.com", "chave não encontrada"))

#popitem
contato3 = {
    "teste@gmail.com": {"nome": "Milito", "idade": 18},
}
print(contato3)
print(contato3.popitem())

#setdefault (adiciono com um valor pre defindido, caso o campo não exista)
pessoa = {"teste@gmail.com": {"nome": "Milito", "idade": 18}}
pessoa.setdefault("nome", "matheus")
print(pessoa) #{"teste@gmail.com": {"nome": "Milito", "idade": 18},}

pessoa.setdefault("telfone", "1111-1111")
print(pessoa) #{"teste@gmail.com": {"nome": "Milito", "idade": 18}, "telfone", "1111-1111"}

#update (atualizando o dicionario)

#values (retornando os valores)
testes = {
    "teste@gmail.com": {"nome": "Milito", "idade": 18},
    "teste2@gmail.com": {"nome": "Silvestre", "idade": 38},
    "teste3@gmail.com": {"nome": "Latitude10", "idade": 28},
}
print(testes.values())

#metodo In
