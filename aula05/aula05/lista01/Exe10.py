# Faça um programa que leia um nome de usuário e a sua senha e não aceite a
# senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando
# a pedir as informações.

usuario = input("Informe ao seu usuario: ")
senha = input("Informe a sua senha: ")

while(usuario == senha):
    print("Senha inválida! Tente novamente")
    usuario = input("Informe ao seu usuario: ")
    senha = input("Informe a sua senha: ")