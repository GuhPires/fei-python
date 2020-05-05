# Programa que mostra a quantidade de tempo necessário (em meses) para que 2 assalariados tenham a
# mesma quantidade de dinheiro ao investir com juros compostos diferentes.
# Author: Gustavo G. Pires
# GitHub: GuhPires

# OBS: Fórmula de juros compostos: S = P(1 + i)^n

from math import pow


# ---- calc_tax ----
# Params: salary -> Float; tax -> Float; n -> Int
# Returns: tax -> Float
# Description: Usa-se a fórmula de juros compostos para calcular os juros após um certo período
# ------------------
def calc_tax(salary, tax, n):
    return salary * pow((1 + (tax/100)), n)


# ---- calc_time ----
# Params: a -> Float; b -> Float
# Returns: time -> Int
# Description: Cálculo de tempo necessário para que o valor de 'b' >= 'a'
# ------------------
def calc_time(a, b):
    a_taxed = a
    b_taxed = b
    counter = 1
    while a_taxed > b_taxed:
        a_taxed = calc_tax(a_taxed, 2, counter)
        b_taxed = calc_tax(b_taxed, 25, counter)
        counter += 1
    return counter


salary_carlos = float(input("Digite o salário de Carlos: "))
print("Tempo necessário:", calc_time(salary_carlos, salary_carlos/2), "meses.")
