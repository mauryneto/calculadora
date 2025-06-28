import os 
import sys

os.system('cls' if os.name == 'nt' else 'clear')

def soma(x,y):
    resultado = x+y
    print(f"\n{x} + {y} = {resultado}\n ")

def subtracao(x,y):
    resultado = x-y
    print(f"\n{x} - {y} = {resultado}\n")

def multiplicacao(x,y):
    resultado = x*y
    print(f"\n{x} * {y} = {resultado}\n")

def divisao(x,y):
    if y == 0:
        print("\nNão é possível dividir por 0\n")
        return
    resultado = x/y
    print(f"\n{x} / {y} = {resultado}\n")

def exponenciacao(x,y):
    resultado = x**y
    print(f"\n{x} elevado a {y} = {resultado}\n")

def operacao(operador,x,y):
    if operador == 0:
        soma(x,y)
    if operador == 1:
        subtracao(x,y)
    if operador == 2:
        multiplicacao(x,y)
    if operador == 3:
        divisao(x,y)
    if operador == 4:
        exponenciacao(x,y) 

def tela():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n0 : Soma")
        print("1 : Subtração")
        print("2 : Multiplicação")
        print("3 : Divisão")
        print("4 : Exponenciação\n")
        try:
            operador = int(input("Escolha a operação que deseja realizar:\n"))
            if operador not in range(5):
                print("Digite um número entre 0 e 4!")
                continue
        except ValueError:
            print("Entrada inválida. Digite um número!\n")
            continue

        print(f"\n>>> Operação escolhida: {['+', '-', '*', '/', '**'][operador]}\n")
        try:
            x = float(input("Qual o primeiro valor?\n"))
            y = float(input("Qual o segundo valor?\n"))
        except ValueError:
            print("Por favor, digite apenas números.\n")
            continue

        operacao(operador, x, y)

        refazer = int(input("Deseja fazer outra operação? 0 - SIM, 1 - NÃO\n"))
        if refazer == 1:
            print("Encerrando a calculadora.")
            sys.exit()
tela()