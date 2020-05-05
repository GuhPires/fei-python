
def calc_taxes(salary):
    deduction = 0
    tax = 0
    if 1499.16 <= salary <= 2246.75:
        deduction = 112.43
        tax = 7.5
    elif 2246.76 <= salary <= 2995.7:
        deduction = 280.94
        tax = 15
    elif 2995.71 <= salary <= 3743.19:
        deduction = 505.62
        tax = 22.5
    elif salary > 3743.19:
        deduction = 692.78
        tax = 27.5

    return (salary * (tax / 100)) - deduction


income = float(input("Digite seu salário: R$ "))

print("O imposto de renda devido é de: R$ %.2f" % calc_taxes(income))