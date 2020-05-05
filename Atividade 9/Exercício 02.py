# Programa que classifica números de 4 algarismos em diferentes tipos dependendo do valor do
# quadrado da soma dos pares adjacentes deste número (ABCD -> AB + CD = E -> E^2 = X),
# classificando-o em 'TIPO I' (X = ABCD), 'TIPO II' (X > ABCD) e 'TIPO III' (X < ABCD)
# Author: Gustavo G. Pires
# GitHub: GuhPires

from math import pow


def calc_squared(number):
    first_pair = number // 100
    last_pair = number % 100
    return pow(first_pair + last_pair, 2)


def fit_type(squared, number):
    grp = ''
    if squared == number:
        grp = 'TIPO I'
    elif squared > number:
        grp = 'TIPO II'
    else:
        grp = 'TIPO III'
    return grp


cond = True
num = 0
while cond:
    num = int(input("Digite um número de 4 algarismos: "))
    if 1000 <= num < 10000:
        cond = False
    else:
        print("Apenas números com 4 algarismos são aceitos, tente novamente...")


sqrd = calc_squared(num)
print(fit_type(sqrd, num))

