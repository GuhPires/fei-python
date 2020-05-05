# Programa que calcula a média aritimética ou ponderada das notas digitadas pelo usuário.
# Author: Gustavo G. Pires
# GitHub: GuhPires

from functools import reduce


def arithmetic_mean(grades):
    result = reduce(lambda a, b: a + b, grades) / len(grades)
    return result


def weighted_mean(grades):
    weights = [5, 3, 2]
    weighted = []
    for idx, grade in enumerate(grades):
        weighted.append(grade * weights[idx])
    result = reduce(lambda a, b: a + b, weighted) / reduce(lambda a, b: a + b, weights)
    return result


def switch_method(grades, method):
    if method in "Aa":
        return arithmetic_mean(grades)
    elif method in "Pp":
        return weighted_mean(grades)
    else:
        print("Nenhum método com a letra informada foi encontrado...")


all_grades = input("Digite as notas separadas por vírgula (EX: 10, 7.8, 9): ")
all_grades = [float(grade.strip()) for grade in all_grades.split(',')]
chosen_method = input("Agora digite um método de média ('A' para aritimética e 'P' para "
                      "ponderada): ")
print("Resultado: %.2f" % switch_method(all_grades, chosen_method))
