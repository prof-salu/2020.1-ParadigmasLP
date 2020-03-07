numero = int(input("Informe um numero: "))

if(numero % 2 == 0):
    print("par")
else:
    print("impar")

idade = int(input("Qual a sua idade? "))

if(idade < 16):
    print("Voce ja pode votar")
elif((idade >= 16 and idade < 18) or idade >= 65):
    print("Voto opcional")
else:
    print("voto obrigatorio")