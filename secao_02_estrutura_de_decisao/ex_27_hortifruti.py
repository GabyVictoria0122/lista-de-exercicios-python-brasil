"""
Exercício 27 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Uma fruteira está vendendo frutas com a seguinte tabela de preços:

                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
receberá ainda um desconto de 10% sobre este total.
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o
valor a ser pago pelo cliente.
Mostre o restultado com duas casas decimais

    >>> calcular_preco_da_compra(2, 0)
    (+)  Morango  - valor:  R$  5.00 - quantidade:  2 kg - preço: R$ 2.50/kg
    (-)  Desconto - valor:  R$  0.00
              Valor Total:  R$  5.00
    >>> calcular_preco_da_compra(6, 0)
    (+)  Morango  - valor:  R$ 13.20 - quantidade:  6 kg - preço: R$ 2.20/kg
    (-)  Desconto - valor:  R$  0.00
              Valor Total:  R$ 13.20
    >>> calcular_preco_da_compra(9, 0)
    (+)  Morango  - valor:  R$ 19.80 - quantidade:  9 kg - preço: R$ 2.20/kg
    (-)  Desconto - valor:  R$  1.98
              Valor Total:  R$ 17.82
    >>> calcular_preco_da_compra(0, 2)
    (+)  Maça     - valor:  R$  3.60 - quantidade:  2 kg - preço: R$ 1.80/kg
    (-)  Desconto - valor:  R$  0.00
              Valor Total:  R$  3.60
    >>> calcular_preco_da_compra(0, 6)
    (+)  Maça     - valor:  R$  9.00 - quantidade:  6 kg - preço: R$ 1.50/kg
    (-)  Desconto - valor:  R$  0.00
              Valor Total:  R$  9.00
    >>> calcular_preco_da_compra(0, 9)
    (+)  Maça     - valor:  R$ 13.50 - quantidade:  9 kg - preço: R$ 1.50/kg
    (-)  Desconto - valor:  R$  1.35
              Valor Total:  R$ 12.15
    >>> calcular_preco_da_compra(2, 2)
    (+)  Morango  - valor:  R$  5.00 - quantidade:  2 kg - preço: R$ 2.50/kg
    (+)  Maça     - valor:  R$  3.60 - quantidade:  2 kg - preço: R$ 1.80/kg
    (-)  Desconto - valor:  R$  0.00
              Valor Total:  R$  8.60
    >>> calcular_preco_da_compra(7, 2)
    (+)  Morango  - valor:  R$ 15.40 - quantidade:  7 kg - preço: R$ 2.20/kg
    (+)  Maça     - valor:  R$  3.60 - quantidade:  2 kg - preço: R$ 1.80/kg
    (-)  Desconto - valor:  R$  1.90
              Valor Total:  R$ 17.10
    >>> calcular_preco_da_compra(7, 7)
    (+)  Morango  - valor:  R$ 15.40 - quantidade:  7 kg - preço: R$ 2.20/kg
    (+)  Maça     - valor:  R$ 10.50 - quantidade:  7 kg - preço: R$ 1.50/kg
    (-)  Desconto - valor:  R$  2.59
              Valor Total:  R$ 23.31

"""


def calcular_preco_da_compra(kilos_de_morango: int, kilos_de_maca: int):
    """Escreva aqui em baixo a sua solução"""


    if 0 < kilos_de_morango <= 5:
        preco_mo = 2.50
    else:
        preco_mo = 2.20

    if 0 < kilos_de_maca <= 5:
        preco_ma = 1.80
    else:
        preco_ma = 1.50

    kg_total = (kilos_de_morango + kilos_de_maca)
    valor_total = (kilos_de_morango * preco_mo) + (kilos_de_maca * preco_ma)

    if kg_total > 8 or valor_total > 25.00:
        desconto = valor_total * 0.1
        valor_total = valor_total - desconto
    else:
        desconto = 0.00



    if kilos_de_maca == 0:
        valor_mo = kilos_de_morango * preco_mo
        resul_valor = f'{valor_mo:.2f}'
        resul_total = f'{valor_total:.2f}'

        print(f'(+)  Morango  - valor:  R$', resul_valor.rjust(5), f'- quantidade:  {kilos_de_morango} kg - preço: R$ {preco_mo:.2f}/kg')
        print(f'(-)  Desconto - valor:  R$  {desconto:.2f}')
        print(f"          Valor Total:  R${resul_total.rjust(6)}")

    if kilos_de_morango == 0:
        valor_ma = kilos_de_maca * preco_ma
        resul_valor = f'{valor_ma:.2f}'
        resul_total = f'{valor_total:.2f}'

        print(f'(+)  Maça     - valor:  R$', resul_valor.rjust(5), f'- quantidade:  {kilos_de_maca} kg - preço: R$ {preco_ma:.2f}/kg')
        print(f'(-)  Desconto - valor:  R$  {desconto:.2f}')
        print(f"          Valor Total:  R${resul_total.rjust(6)}")

    if kilos_de_maca != 0 and kilos_de_morango != 0:
        valor_ma = kilos_de_maca * preco_ma
        valor_mo = kilos_de_morango * preco_mo
        resul_valor_ma = f'{valor_ma:.2f}'
        resul_valor_mo = f'{valor_mo:.2f}'
        resul_total = f'{valor_total:.2f}'


        print(f'(+)  Morango  - valor:  R$', resul_valor_mo.rjust(5), f'- quantidade:  {kilos_de_morango} kg - preço: R$ {preco_mo:.2f}/kg')
        print(f'(+)  Maça     - valor:  R$', resul_valor_ma.rjust(5), f'- quantidade:  {kilos_de_maca} kg - preço: R$ {preco_ma:.2f}/kg')
        print(f'(-)  Desconto - valor:  R$  {desconto:.2f}')
        print(f"          Valor Total:  R${resul_total.rjust(6)}")

