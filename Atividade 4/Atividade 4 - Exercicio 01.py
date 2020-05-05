
def calc_total_kits(a, b, c):
    if a < 4 or b < 3 or c < 5:
        return 0
    return min([a // 4, b // 3, c // 5])


det = int(input("Digite a quantidade de detergente: "))
sab = int(input("Digite a quantidade de sabão em pó: "))
esp = int(input("Digite a quantidade de esponja: "))

total_kits = calc_total_kits(det, sab, esp)

print("Quantidade de kits: ", total_kits)
