from Ex07_funcoes import *

categoria = escolher_categoria()
tamanho = escolher_tamanho_pizza()


if categoria == 1:
    preco = calcular_preco_pizza_normal(tamanho)

elif categoria == 2:
    preco = calcular_preco_pizza_gourmet(tamanho)

else:
    preco = calcular_preco_pizza_premium(tamanho)

print(f'O tamanho da pizza selecionada foi {categoria} e seu valor é de R$ {preco}')