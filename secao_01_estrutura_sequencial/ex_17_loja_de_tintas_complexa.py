"""
Exercício 17 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e
que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o custo seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

    >>> from secao_01_estrutura_sequencial import ex_17_loja_de_tintas_complexa
    >>> ex_17_loja_de_tintas_complexa.input = lambda k: '100'
    >>> ex_17_loja_de_tintas_complexa.calcular_latas_e_preco_de_tinta()
    Você deve comprar 19 litros de tinta.
    Você pode comprar 2 lata(s) de 18 litros a um custo de R$ 160. Vão sobrar 17.0 litro(s) de tinta.
    Você pode comprar 6 lata(s) de 3.6 litros a um custo de R$ 150. Vão sobrar 2.6 litro(s) de tinta.
    Para menor custo, você pode comprar 1 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 105. Vão sobrar 2.6 litro(s) de tinta.
    >>> ex_17_loja_de_tintas_complexa.input = lambda k: '200'
    >>> ex_17_loja_de_tintas_complexa.calcular_latas_e_preco_de_tinta()
    Você deve comprar 37 litros de tinta.
    Você pode comprar 3 lata(s) de 18 litros a um custo de R$ 240. Vão sobrar 17.0 litro(s) de tinta.
    Você pode comprar 11 lata(s) de 3.6 litros a um custo de R$ 275. Vão sobrar 2.6 litro(s) de tinta.
    Para menor custo, você pode comprar 2 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 185. Vão sobrar 2.6 litro(s) de tinta.

"""


def calcular_latas_e_preco_de_tinta():
    """Escreva aqui em baixo a sua solução"""

    tamanho = float(input('Insira o tamanho em metros quadrados da área a ser pintada'))
    tamanho_folga = (tamanho * 1.1)
    litros_tinta = round((tamanho_folga/6) + 0.5)

#Situação 1: latas
    q_latas = round((litros_tinta / 18)+0.5)
    custo_latas = int(q_latas * 80.00)
    sobra_latas = (q_latas * 18) - litros_tinta


#Situação 2: galoes
    q_galoes = round((litros_tinta / 3.6) + 0.5)
    custog= int(q_galoes * 25.00)
    sobrag = (q_galoes * 3.6) - litros_tinta
#

# Situação 3: latas e galoes
    q_misturaL = int(litros_tinta // 18)
    q_misturaG = ((litros_tinta-q_misturaL *18) )
    custo_mistura = (q_misturaL*80) + (q_misturaG*25)
    sobra_mistura = ((q_misturaG*3.6) + (q_misturaL*18)) - litros_tinta



    print(f'Você deve comprar {litros_tinta} litros de tinta.')
    print(f'Você pode comprar {q_latas} lata(s) de 18 litros a um custo de R$ {custo_latas}. Vão sobrar {sobra_latas:.1f} litro(s) de tinta.')
    print(f'Você pode comprar {q_galoes} lata(s) de 3.6 litros a um custo de R$ {custog}. Vão sobrar {sobrag:.1f} litro(s) de tinta.')
    print(f'Para menor custo, você pode comprar {q_misturaL} lata(s) de 18 litros e {q_misturaG} galão(ões) de 3.6 litros a um custo de R$ {custo_mistura}. Vão sobrar {sobra_mistura:.1f} litro(s) de tinta.')