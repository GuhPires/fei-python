# Programa que calcula a média do diâmetro das peças (em mm).
# Author: Gustao G. Pires
# GitHub: GuhPires

from functools import reduce


def calc_avg(values):
    return reduce(lambda a, b: a + b, values) / len(values)


num_arr = []
for i in range(10):
    num = float(input("Digite o diâmetro (em mm): "))
    num_arr.append(num)

print("Média das medidas: %.3f" % calc_avg(num_arr))
