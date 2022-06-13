"""
Exercício 04 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a
população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o
número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas
de crescimento.

    >>> calcular_ano_ultrapassagem_populacional()
    'População de A, depois de 63 ano(s) será de 515033 pessoas, superando a de B, que será de 510964 pessoas'


"""


def calcular_ano_ultrapassagem_populacional() -> str:
    """Escreva aqui em baixo a sua solução"""

    inicio_A = 80000
    inicio_B = 200000
    tc_A = 1.03
    tc_B = 1.015
    ano = 0

    while inicio_A < inicio_B:
        inicio_A = inicio_A * tc_A
        inicio_B = inicio_B * tc_B
        ano += 1

    print(f"'População de A, depois de {ano} ano(s) será de {inicio_A:.0f} pessoas, superando a de B, que será de {inicio_B:.0f} pessoas'")

 # feito