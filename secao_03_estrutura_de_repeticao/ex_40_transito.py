"""
Exercício 40 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os
1) seguintes dados:
2) Código da cidade;
3) Número de veículos de passeio (em 1999);
4) Número de acidentes de trânsito com vítimas (em 1999).

Deseja-se saber:

1) Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
2) Qual a média de veículos nas cinco cidades juntas;
3) Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

Mostre os valores com uma casa decimail

    >>> calcular_estatisticas(('SJC', 190_000, 300), ('SP', 1_000_000, 2_000 ),
    ... ('BH', 800_000, 1000), ('FZ', 600_000, 700), ('FL', 150_000, 900)
    ... )
    O maior índice de acidentes é de FL, com 6.0 acidentes por mil carros.
    O menor índice de acidentes é de FZ, com 1.2 acidentes por mil carros.
    O média de veículos por cidade é de 548000.
    A média de acidentes total nas cidades com menos de 150 mil carros é de 900.0 acidentes.
"""


def calcular_estatisticas(*cidades):
    """Escreva aqui em baixo a sua solução"""

    indice_maior = indice_menor = media = None
    soma_car = soma_acid = quant = 0

    """Resolução Item 1) Qual o maior e menor índice de acidentes de transito e a que cidade pertence;"""

    for (cod, quant_car, quant_acid) in cidades:
        indice = quant_acid / quant_car
        if indice_maior == None or indice_maior < indice:
            indice_maior = indice
            cod_maior = cod
        if indice_menor == None or indice_menor > indice:
            indice_menor = indice
            cod_menor = cod

    indice_maior *= 1000
    indice_menor *= 1000

    """Resolução Item 2) Qual a média de veículos nas cinco cidades juntas;"""

    for (cod, quant_car, quant_acid) in cidades:
        soma_car += quant_car
        if quant_car <= 150_000:
            soma_acid += quant_acid
            quant += 1

    media_car = soma_car / len(cidades)

    """Resolução Item 3) Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio."""


    media_acid = soma_acid / quant


    print(f"""O maior índice de acidentes é de {cod_maior}, com {indice_maior} acidentes por mil carros.
O menor índice de acidentes é de {cod_menor}, com {indice_menor:.1f} acidentes por mil carros.
O média de veículos por cidade é de {media_car:.0f}.
A média de acidentes total nas cidades com menos de 150 mil carros é de {media_acid} acidentes.""")

    #feito
