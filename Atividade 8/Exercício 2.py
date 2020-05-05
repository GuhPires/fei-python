# Programa que calcula o valor de E (E = 1 + 1/1 + 1/2 + 1/3 + ... + 1/n)
# Author: Gustavo G. Pires
# GitHub: GuhPires

# Utilizando recursividade para resolver o problema proposto:


# ---- calc_e ----
# Params: n -> Integer; init_val -> Float
# Returns: e -> Float
# Description: Função principal que recebe um input do usuário com o 'n' requerido e usa
# recursividade para calcular E
# -----------------
def calc_e(n, init_val=1):
    e = init_val + 1 / n
    if n == 1:
        return e
    else:
        counter = n - 1
        return calc_e(counter, e)


num = int(input("Digite o valor de N: "))
final_e = calc_e(num)
print("O valor de E: %0.2f" % final_e)
