# 2) Desenvolva uma função que receba dois números inteiros e retorne o maior entre eles.

def receber_maior (num1: int, num2: int) -> int:
    if num1 > num2:
        return num1

    return num2

num1 = int(input('Informe um número: '))
num2 = int(input('Informe um outro número número: '))
maior = receber_maior(num1, num2)
print(f'O maior número digitado é {maior}')