# Dicionários são estruturas poderosas e que acessamos os seus elementos através de chaves e não de sua posição.

pessoa1 = {"nome" : "Jessica", "idade" : 21, "sexo" : "Feminino", "profissao" : "Estudante"}
pessoa2 = {'nome' : '', 'idade' : 29, 'sexo' : 'Masculino', 'profissao' : 'Bancario'}


print(pessoa1)
print(pessoa2)
# Qualquer chave de um dicionário é associada (ou mapeada) a um valor.
# Os valores podem ser qualquer tipo de dado do Python.
# Portanto, os dicionários são pares de chave-valor não ordenados.

print(pessoa1["nome"])
print(pessoa2['profissao'])

# Se precisarmos adicionar algum elemento, por exemplo, o telefone, basta fazermos:

pessoa1["telefone"] = "12345678"
pessoa1["celular: "] = "9999999"

print(pessoa1)

# Como sempre acessamos seus elementos através de chaves, o dicionário possui um método chamado keys()
# que devolve o conjunto de suas chaves:
print(pessoa1.keys())

# Assim como um método chamado values() que retorna seus valores:
print(pessoa1.values())

print(pessoa1["telefone"])

print(pessoa1)