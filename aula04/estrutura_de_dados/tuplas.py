# Uma tupla é definida de forma parecida com uma lista com a diferença do delimitador.
# Enquanto listas utilizam colchetes como delimitadores, as tuplas usam parênteses.

dias = ("Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado")
print(type(dias))

# Uma tupla é uma lista imutável, ou seja, uma tupla é uma sequência que não pode ser alterada depois de criada.
# O método append() da lista não existe na tupla
dias.append("Domingo extra")

# As regras para os índices são as mesmas das listas
print(dias[0])
print(dias[4])

# As tuplas são imutáveis e geralmente contêm uma sequência heterogênea de elementos
# já as listas são mutáveis e seus elementos geralmente são homogêneos e são acessados ​​pela iteração da lista.
