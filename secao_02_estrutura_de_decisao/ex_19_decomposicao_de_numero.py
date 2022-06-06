"""
Exercício 19 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do
mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

    >>> decompor_numero(1000)
    'O número precisa ser menor que 1000'
    >>> decompor_numero(-1)
    'O número precisa ser positivo'
    >>> decompor_numero(326)
    '326 = 3 centenas, 2 dezenas e 6 unidades'
    >>> decompor_numero(300)
    '300 = 3 centenas'
    >>> decompor_numero(100)
    '100 = 1 centena'
    >>> decompor_numero(320)
    '320 = 3 centenas e 2 dezenas'
    >>> decompor_numero(310)
    '310 = 3 centenas e 1 dezena'
    >>> decompor_numero(305)
    '305 = 3 centenas e 5 unidades'
    >>> decompor_numero(301)
    '301 = 3 centenas e 1 unidade'
    >>> decompor_numero(311)
    '311 = 3 centenas, 1 dezena e 1 unidade'
    >>> decompor_numero(111)
    '111 = 1 centena, 1 dezena e 1 unidade'
    >>> decompor_numero(101)
    '101 = 1 centena e 1 unidade'
    >>> decompor_numero(25)
    '25 = 2 dezenas e 5 unidades'
    >>> decompor_numero(20)
    '20 = 2 dezenas'
    >>> decompor_numero(21)
    '21 = 2 dezenas e 1 unidade'
    >>> decompor_numero(10)
    '10 = 1 dezena'
    >>> decompor_numero(16)
    '16 = 1 dezena e 6 unidades'
    >>> decompor_numero(1)
    '1 = 1 unidade'
    >>> decompor_numero(7)
    '7 = 7 unidades'

"""


def decompor_numero(numero: int):
    """Escreva aqui em baixo a sua solução"""

    cen_int = int(numero // 100)
    dez_int = int(numero // 10%10)
    uni_int = int(numero //1%10)

    cen_str = dez_str = uni_str = ''

    conta_num = 0

    if cen_int == 1:
        cen_str = '1 centena'
        conta_num += 1
    elif cen_int > 1:
        cen_str = f'{cen_int} centenas'
        conta_num += 1

    if dez_int == 1:
        dez_str = '1 dezena'
        conta_num += 1
    elif dez_int > 1:
        dez_str = f'{dez_int} dezenas'
        conta_num += 1

    if uni_int == 1:
        uni_str = '1 unidade'
        conta_num += 1
    elif uni_int > 1:
        uni_str = f'{uni_int} unidades'
        conta_num += 1




    if numero <= 0:
        print("'O número precisa ser positivo'")
    elif numero >= 1000:
        print(f"'O número precisa ser menor que 1000'")
    elif conta_num == 1:
        print(f"'{numero} = {cen_str + dez_str + uni_str}'")
    elif conta_num == 2:
        if cen_str != '':
            segunda_part = dez_str + uni_str
            print(f"'{numero} = {cen_str} e {segunda_part}'")
        else:
             print(f"'{numero} = {dez_str} e {uni_str}'")
    elif conta_num == 3:
        print(f"'{numero} = {cen_str}, {dez_str} e {uni_str}'")
