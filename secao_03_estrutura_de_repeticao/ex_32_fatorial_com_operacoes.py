"""
Exercício 32 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
Ex.: 5!=5.4.3.2.1=120

    >>> calcular_fatorial(1)
    Fatorial de 1:
    1! = 1 = 1
    >>> calcular_fatorial(2)
    Fatorial de 2:
    2! = 2 . 1 = 2
    >>> calcular_fatorial(3)
    Fatorial de 3:
    3! = 3 . 2 . 1 = 6
    >>> calcular_fatorial(4)
    Fatorial de 4:
    4! = 4 . 3 . 2 . 1 = 24
    >>> calcular_fatorial(5)
    Fatorial de 5:
    5! = 5 . 4 . 3 . 2 . 1 = 120

"""


def calcular_fatorial(n: int):
    """Escreva aqui em baixo a sua solução"""

    expo = n
    lista_n = []
    if type(n) == int and n > 0:
        if n == 1:
            print(f"Fatorial de {n}:")
            print(f"{n}! = {n} = {n}")
        else:
            primeiro_n = n
            while n > 1:
                expo = (expo * (n-1))
                n -= 1
                lista_n.append(n)

            print_lista = ' . '.join(map(str, lista_n))

            print(f"Fatorial de {primeiro_n}:")
            print(f"{primeiro_n}! = {primeiro_n} . {print_lista} = {expo}")
