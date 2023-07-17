"""
Exercício 24 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da
operação deve ser acompanhado de uma frase que diga se o número é:
  par ou ímpar;
  positivo ou negativo;
  inteiro ou decimal.

Mostre o restultado com duas casas decimais

    >>> fazer_operacao_e_classificar(2, 3, '+')
    Resultado: 5.00
    Número é impar, positivo e inteiro.
    >>> fazer_operacao_e_classificar(-4, 2, '/')
    Resultado: -2.00
    Número é par, negativo e inteiro.
    >>> fazer_operacao_e_classificar(0, 2, '*')
    Resultado: 0.00
    Número é par, neutro e inteiro.
    >>> fazer_operacao_e_classificar(-3.14, 2, '*')
    Resultado: -6.28
    Número é negativo e decimal.
    >>> fazer_operacao_e_classificar(3.14, 2, '-')
    Resultado: 1.14
    Número é positivo e decimal.

"""


def fazer_operacao_e_classificar(n_1: float, n_2: float, operacao: str):
    """Escreva aqui em baixo a sua solução"""

    resultado = 0
    if operacao == '+':
        resultado = n_1 + n_2
    elif operacao == '-':
        resultado = n_1 - n_2
    elif operacao == '*':
        resultado = n_1 * n_2
    elif operacao == '/':
        resultado = n_1 / n_2

    par = resultado % 2
    p_i = ''


    if resultado > 0:
        p_n_n = 'positivo'
    elif resultado < 0:
        p_n_n = 'negativo'
    else:
        p_n_n = 'neutro'

    inteiro = resultado//1
    if inteiro == resultado:
        i_d = 'inteiro'
        if par == 0:
            p_i = 'par, '
        else:
            p_i = 'impar, '
    else:
        i_d = 'decimal'


    print(f'Resultado: {resultado:.2f}')
    print(f'Número é {p_i}{p_n_n} e {i_d}.')
