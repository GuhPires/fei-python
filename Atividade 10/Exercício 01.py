# Programa que soma números de uma sequência (2 + 4/3 + 6/5 + 8/7 + ...) até um número inteiro
# positivo dado pelo usuário.
# Author: Gustavo G. Pires
# GitHub: GuhPires


def calc_seq(iterator):
    formula = iterator * 2
    num = formula / (formula - 1)
    return num


def soma_n(a):
    counter = 1
    S = 0
    while counter <= a:
        S += calc_seq(counter)
        counter += 1
    return S


cond = True
number = 0

while cond:
    number = int(input("Digite um número inteiro positivo: "))
    if number <= 0:
        print("Número precisa ser positivo, tente novamente...")
    else:
        cond = False

print("O resltado da soma da sequência é: %.2f" % soma_n(number))
