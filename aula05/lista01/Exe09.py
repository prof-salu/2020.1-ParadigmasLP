# Faça um programa que peça uma nota, entre zero e dez. Mostre uma
# mensagem caso o valor seja inválido e continue pedindo até que o usuário
# informe um valor válido.

nota = float(input("Informe uma nota: "))

if(nota >= 0 and nota <= 10):
    print("Nota:", nota)
else:
    while(nota < 0 or nota > 10):
        print("Nota inválida!")
        nota = float(input("Informe uma nota: "))


    