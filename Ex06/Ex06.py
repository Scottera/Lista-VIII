from Ex06_funcoes import calcular_grau_aco

carbono = float(input('Informe o conteúdo do carbono: '))
rokwell = float(input('Informe a dureza do Rokwell: '))
resist = float(input('Informe a resistência: '))

result = calcular_grau_aco(carbono, rokwell, resist)

print(f'O grau deste aço é {result}!')