# listas -> Uma lista é uma sequência de valores onde cada valor é identificado por um índice iniciado por 0.

lista1 = [1,2,3,4,5]
print(type(lista1))
print(lista1)

# listas não precisam necessariamente conter elementos de mesmo tipo.
lista2 = [1,2,3,"Carlos", 4.5, True]
print(lista2)

# Além de acessar um valor específico utilizando o índice, podemos acessar múltiplos valores através do fatiamento.
lista3 = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]

# imprime o terceiro valor da lista
print(lista3[3])
# imprime os quatros primeiros elementos
print(lista3[:4])
# imprime o intervalo entre as posicoes 1 e 3
print(lista3[1:6])

# As listas também possuem funcionalidades prontas e podemos manipulá-las através de funções embutidas.
# A lista tem uma função chamada append() que adiciona um dado na lista

lista4 = ["Ana", "Maria"]
print(lista4)
lista4.append("Mauro")
print(lista4)

# A lista tem uma função chamada remove() que remove um dado na lista
lista4.remove("Maria")
print(lista4)

#Isso é possível já que listas são sequências mutáveis, ou seja conseguimos adicionar, remover e modificar seus elementos.



