# Programa que calcula as médias aritimética, harmônica e geométrica dos algarismos que compõe um
# número e mostra qual a maior média obtida.
# Author: Gustavo G. Pires
# GitHub: GuhPires

from math import pow


# ---- separate_numbers ----
# Params: num -> Integer
# Returns: splitted -> Dictionary<String: Integer>
# Description: Função genérica (funciona para números com qualquer quantidade de algarismos) Para
# que suporte mais algarismos, aumente as unidades em 'split_type'.
# --------------------------
def separate_numbers(num):
    num_remainder = num
    condition = True
    counter = 0
    split_type = ['units', 'tens', 'hundreds']
    splitted = {}
    while condition:
        remainder = num_remainder % 10
        num_remainder -= remainder
        num_remainder /= 10
        splitted[split_type[counter]] = int(remainder)
        if counter + 1 == len(split_type):
            condition = False
        else:
            counter += 1
    return splitted


# ---- calc_arithmetic_mean ----
# Params: *args -> Integers
# Returns: mean -> Float
# Description: Função genérica para cálculo de média aritmética (funciona para qualquer quantidade
# de números, graças ao *args)
# ------------------------------
def calc_arithmetic_mean(*args):
    sum = 0
    for arg in args:
        sum += arg
    mean = sum / len(args)
    # print("Arithmetic: ", mean)
    return mean


# ---- calc_harmonic_mean ----
# Params: *args -> Integers
# Returns: mean -> Float
# Description: Função genérica para cálculo de média harmônica (funciona para qualquer quantidade
# de números, graças ao *args)
# ------------------------------
def calc_harmonic_mean(*args):
    sum = 0
    for arg in args:
        if arg > 0:
            sum += (1/arg)
    mean = len(args) / sum
    # print("Harmonic: ", mean)
    return mean


# ---- calc_geometric_mean ----
# Params: *args -> Integers
# Returns: mean -> Float
# Description: Função genérica para cálculo de média geométrica (funciona para qualquer quantidade
# de números, graças ao *args)
# ------------------------------
def calc_geometric_mean(*args):
    product = 1
    for arg in args:
        product *= arg
    mean = pow(product, 1/len(args))
    # print("Geometric: ", mean)
    return mean


number = int(input("Digite um número inteiro de 3 digitos: "))

if 100 <= number <= 999:
    numbers_separated = separate_numbers(number)
    arithmetic = calc_arithmetic_mean(numbers_separated['units'], numbers_separated['tens'],
                                      numbers_separated['hundreds'])
    print("Média aritimética:", arithmetic)

    harmonic = calc_harmonic_mean(numbers_separated['units'], numbers_separated['tens'],
                                  numbers_separated['hundreds'])
    print("Média harmônica:", harmonic)

    geometric = calc_geometric_mean(numbers_separated['units'], numbers_separated['tens'],
                                    numbers_separated['hundreds'])
    print("Média geométrica:", geometric)

    print("A maior média é:", max(arithmetic, harmonic, geometric))
else:
    print("O número digitado não contém 3 algarismos...")
