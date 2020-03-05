# -*- coding: utf-8 -*-

idade = int(input("Informe a sua idade: "))
futuro = 10

print("A sua idade daqui {0} anos sera de {1} anos".format(futuro, (idade + futuro)))

# imprimindo todos os valores na mesma linha
print(1,2,3,4,5, end="")
#pulando uma linha
print()

# imprimindo todos os valores na mesma linha separados por @
print(1,2,3,4,5, end="", sep="@")