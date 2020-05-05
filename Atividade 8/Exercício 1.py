# Programa que obtem o valor médio das medidas especificadas pelo usuário
# Author: Gustavo G. Pires
# GitHub: GuhPires

# Utilizando recursividade para resolver o problema proposto:

# ---- calc_avg ----
# Params: diameters -> List[float]
# Returns: avg -> Float
# Description: Função principal que recebe um input do usuário com o valor da peça utilizando
# recursividade e calcula a média das medidas
# -------------------
import functools


def calc_avg(diameters):
    diameter = float(input("Digite o valor do diâmetro: "))
    diameters.append(diameter)
    if diameters[len(diameters) - 1] == 0:
        return (functools.reduce(lambda a, b: a + b, diameters))/float(len(diameters) - 1)
    else:
        return calc_avg(diameters)


average = calc_avg([])
print("Média dos diâmetros:", average)
