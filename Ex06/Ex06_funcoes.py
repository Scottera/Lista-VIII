def calcular_grau_aco (carbono: float, rokwell: float, resist: float):
    if carbono < 7 and rokwell > 50 and resist > 80000:
        return 10
    elif carbono < 7 and rokwell > 50:
        return 9
    elif carbono < 7:
        return 8
    else:
        return 7