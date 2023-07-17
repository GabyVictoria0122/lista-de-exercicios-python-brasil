"""
Exercício 23 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

    >>> primos, divisoes = calcular_primos_e_divisoes(0)
    >>> primos
    ''
    >>> divisoes
    0
    >>> primos, divisoes = calcular_primos_e_divisoes(1)
    >>> primos
    ''
    >>> divisoes
    0
    >>> primos, divisoes = calcular_primos_e_divisoes(2)
    >>> primos
    '2'
    >>> divisoes
    0
    >>> primos, divisoes = calcular_primos_e_divisoes(3)
    >>> primos
    '2, 3'
    >>> divisoes <= 1
    True
    >>> primos, divisoes = calcular_primos_e_divisoes(4)
    >>> primos
    '2, 3'
    >>> divisoes <= 3
    True
    >>> primos, divisoes = calcular_primos_e_divisoes(5)
    >>> primos
    '2, 3, 5'
    >>> divisoes <= 6
    True

"""
from typing import Tuple


def calcular_primos_e_divisoes(n: int) -> Tuple[str, int]:
    """Escreva aqui em baixo a sua solução"""

    # i = eh_primo(n)
    # return (imprimir_primos(n), i )
    divisoes = nro_divisoes(n)
    return (imprimir_primos(n), divisoes)

def imprimir_primos(n):

    primos = []
    for num in range(2, n+1):
        if is_prime(num):
            primos.append(str(num))

    return ', '.join(primos)




# def eh_primo(n):

    # i = 0
    # for v in range(1, n + 1):
    #     if n % v == 0:
    #         i += 1
    # if i != 2:
    #     return False
    # return True

def is_prime(n):
    """retorna se o número é primo"""
    prime = True
    for num in range(2, n):
        resto_divisao = n % num
        if resto_divisao == 0:
            prime = False
            break
    return prime

def nro_divisoes(n):
    """retorna se o número é primo"""
    divisoes = 0
    for num in range(2, n):
        divisoes += 1

    return divisoes

#feito com help do Roger





















































