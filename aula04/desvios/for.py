# imprimir todos os numeros pares no intervalo de 0 a 100

for numero in range (0, 101):
    if(numero % 2 == 0):
        print(numero, end=" ")

print()

# imprimir todos os multiplos de 3 no intervalo de 0 a 100

for numero in range (0, 100, 3):
    print(numero, end=" ")

# Com a função range() podemos definir um step (um passo), que é o intervalo entre os elementos.
# Por padrão o step tem valor igual a 1 mas podemos alterar este valor passando um terceiro parâmetro para a função

print()
for lista in ["ana", "clara", "bob", "bia", "gabi"]:
    print(lista, end=" ")

