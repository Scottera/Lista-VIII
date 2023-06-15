from Ex08 import *


opcao = 0

while opcao != 3:
    opcao = escolher_opcao()

    if opcao == 1:
        tratar_combinacoes()

    elif opcao == 2:
        tratar_arranjos()

    elif opcao != 3:
        print('Opção inválida!')

    