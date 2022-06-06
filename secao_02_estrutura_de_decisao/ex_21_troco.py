"""
Exercício 21 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar
quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo
é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma
nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10,
uma nota de 5 e quatro notas de 1.

    >>> calcular_troco(256)
    '2 notas de R$ 100, 1 nota de R$ 50, 1 nota de R$ 5 e 1 nota de R$ 1'
    >>> calcular_troco(1)
    '1 nota de R$ 1'
    >>> calcular_troco(5)
    '1 nota de R$ 5'
    >>> calcular_troco(10)
    '1 nota de R$ 10'
    >>> calcular_troco(11)
    '1 nota de R$ 10 e 1 nota de R$ 1'
    >>> calcular_troco(399)
    '3 notas de R$ 100, 1 nota de R$ 50, 4 notas de R$ 10, 1 nota de R$ 5 e 4 notas de R$ 1'
"""


def calcular_troco(valor: int) -> str:
    """Escreva aqui em baixo a sua solução"""

    cen_int = int(valor // 100)
    dez_int = int(valor // 10 % 10)
    uni_int = int(valor // 1 % 10)
    cen_str = dez_str = uni_str = ''
    conta_nota = 0

    if cen_int == 1:
        cen_str = '1 nota de R$ 100'
        conta_nota += 1
    elif 0 < cen_int > 1:
        cen_str = f'{cen_int} notas de R$ 100'
        conta_nota += 1

    if dez_int == 5:
        dez_str = '1 nota de R$ 50'
        conta_nota += 1
    elif dez_int > 5:
        notas_10 = dez_int - 5
        dez_str = '1 nota de R$ 50'
        conta_nota += 1
        if notas_10 == 1:
            notas_10_str = f'{notas_10} nota de R$ 10'
            conta_nota += 1
        else:
            notas_10_str = f'{notas_10} notas de R$ 10'
            conta_nota += 1
    elif 0 < dez_int < 5:
        if dez_int == 1:
            dez_str = f'{dez_int} nota de R$ 10'
            conta_nota += 1
        else:
            dez_str = f'{dez_int} notas de R$ 10'
            conta_nota += 1

    if uni_int == 5:
        uni_str = '1 nota de R$ 5'
        conta_nota += 1
    elif 0 < uni_int < 5:
        if uni_int == 1:
            uni_str = f'{uni_int} nota de R$ 1'
            conta_nota += 1
        else:
            uni_str = f'{uni_int} notas de R$ 1'
            conta_nota += 1
    elif uni_int > 5:
        uni_str = '1 nota de R$ 5'
        conta_nota += 1
        nota_1 = uni_int - 5
        if nota_1 == 1:
            nota_1_str = f'{nota_1} nota de R$ 1'
            conta_nota += 1
        else:
            nota_1_str = f'{nota_1} notas de R$ 1'
            conta_nota += 1


    if conta_nota == 1:
        print(f"'{cen_str}{dez_str}{uni_str}'")
    elif conta_nota == 2:
        if cen_str == '':
            print(f"'{dez_str} e {uni_str}'")
        elif cen_str != '':
            segunda_parte = dez_str + uni_str
            print(f"'{cen_str} e {segunda_parte}'")

    elif conta_nota == 3:
        print(f"'{cen_str}, {dez_str} e {uni_str}'")
    elif conta_nota == 4:
        if dez_int > 5:
            print(f"'{cen_str}, {dez_str}, {notas_10_str} e {uni_str}'")
        elif uni_int > 5:
            print(f"'{cen_str}, {dez_str}, {uni_str} e {nota_1_str}'")

    elif conta_nota == 5:
        print(f"'{cen_str}, {dez_str}, {notas_10_str}, {uni_str} e {nota_1_str}'")