def calcular_preco_pizza_normal(tamanho: int) -> int:
    if tamanho == 1:
        return 15
    elif tamanho == 2:
        return 15 + 3
    else:
        return 15 + 6



def calcular_preco_pizza_gourmet (tamanho: int) -> int:
    if tamanho == 1:
        return 20
    elif tamanho == 2:
        return 20 + 4
    else:
        return 20 + 8


def calcular_preco_pizza_premium (tamanho: int) -> int:
    if tamanho == 1:
        return 30
    elif tamanho == 2:
        return 30 + 6
    else:
        return 30 + 12


def escolher_categoria() -> int:
    print('Informe a categoria desejada, sabendo que: \n'
          '1- Pizza Normal \n'
          '2- Pizza Gourmet \n'
          '3- Pizza Premium')

    return int(input('==> '))

def escolher_tamanho_pizza() -> int:
    print('Informe o tamanho da pizza, sendo: \n'
          '1- M\n'
          '2- G\n'
          '3- GG')

    return int(input('==> '))