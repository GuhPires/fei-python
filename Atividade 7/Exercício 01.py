# Programa que devolve o "espelho" de um número apresentado
# Author: Gustavo G. Pires
# GitHub: GuhPires


# ---- mirror_numbers ----
# Params: num -> Integer
# Returns -> num_arr -> Integer
# Description: Função genérica para inverter a ordem dos algarismos em um número
# ------------------------
def mirror_numbers(num):
    start_num = num
    num_arr = []
    while True:
        remainder = start_num % 10
        start_num -= remainder
        start_num /= 10
        num_arr.insert(len(num_arr), str(int(remainder)))
        if start_num == 0:
            break
    return int(''.join(num_arr))


number = int(input("Digite o número inteiro: "))
print("Algarismos invertidos:", mirror_numbers(number))
