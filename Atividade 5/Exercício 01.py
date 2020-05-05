
def choose_tv(dist, model):
    if model == 100:
        if dist <= 1.4:
            return 32
        elif 1.5 <= dist <= 2.6:
            return 37
        else:
            return 42

    elif model == 200:
        if dist <= 2.8:
            return 32
        elif 2.9 <= dist <= 3.6:
            return 50
        else:
            return 61


def userPrompt():
    distance = float(input("Digite a distância: "))
    tv_model = int(input("Digite a série: "))

    if tv_model != 100 and tv_model != 200:
        print("Modelo de TV inexistente, por favor tente novamente...")
        userPrompt()
    else:
        print("Tamanho da televisão: ", choose_tv(distance, tv_model))


userPrompt()

