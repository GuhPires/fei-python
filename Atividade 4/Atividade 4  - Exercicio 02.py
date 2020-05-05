
def calc_bonus(y, s):
    rate = 2.5
    if y > 3:
        rate += (y - 3) * 1.7
    return s * (rate / 100)


years = float(input("Digite quantos anos está nesta empresa: "))
salary = float(input("Digite seu salário atual: "))

bonus = calc_bonus(years, salary)

print("Seu adicional será de: R$ %.2f" % bonus)
