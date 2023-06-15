from Ex05_funcao import calcular_circulo, calcular_quadrado, calcular_triangulo

opcao = int(input('Informe uma opção: '))

if opcao == 1:
    lado = float(input('Informe o tamanho do lado do quadrado: '))
    print(f'A área do quadrado é de {calcular_quadrado(lado)}')
elif opcao == 2:
    raio = float(input('Informe o raio da circunferência: '))
    print(f'A área do círculo é de {calcular_circulo(raio)}')
elif opcao == 3:
    base = float(input('Informe a base do triângulo: '))
    altura = float(input('Informe a altura do triângulo: '))
    print(f'A área do triângulo é de {calcular_triangulo(base, altura)}')
else:
    print('Opção inválida.')