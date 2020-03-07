#importando modulos
import random

#Criando a funcoes

#Para definirmos uma função no Python utilizamos o comando def

#Sem parametros e sem retorno
def exibirMensagem():
    print("Bem vindos a aula de Paradigmas de LP")

#Com parametro e sem retorno
def imprimirSaudacao(nome):
    print("Ola {}, tudo bem com vc?".format(nome))

#Sem parametros e com retorno
def sorteiaNumero():
    return (random.randint(1, 100))

# com parametros e com retorno
def somaNum(a,b):
    return (a + b)



### Executando as funcoes
exibirMensagem()

imprimirSaudacao("João")

print(somaNum(5,7))

print(sorteiaNumero())