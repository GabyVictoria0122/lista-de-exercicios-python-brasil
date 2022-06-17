"""
Exercício 43 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

O cardápio de uma lanchonete é o seguinte:

Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00

Faça um programa que receba os itens pedidos e as quantidades desejadas.
Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido e quantidade de itens
comprados.


    >>> fechar_conta()
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |          0 |       0.00 |
    -----------------------------------------------------------------------------
    >>> fechar_conta(('100', 1))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          1 |       1.20 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |          1 |       1.20 |
    -----------------------------------------------------------------------------
    >>> fechar_conta(('100', 1), ('100', 2))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          3 |       3.60 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |          3 |       3.60 |
    -----------------------------------------------------------------------------
    >>> fechar_conta(('100', 1), ('100', 2), ('101', 2))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          3 |       3.60 |
    | Bauru Simples    | 101    | 1.30                |          2 |       2.60 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |          5 |       6.20 |
    -----------------------------------------------------------------------------
    >>> fechar_conta(('100', 1), ('100', 2), ('101', 2), ('102', 3))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          3 |       3.60 |
    | Bauru Simples    | 101    | 1.30                |          2 |       2.60 |
    | Bauru com Ovo    | 102    | 1.50                |          3 |       4.50 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |          8 |      10.70 |
    -----------------------------------------------------------------------------
    >>> fechar_conta(('100', 1), ('100', 2), ('101', 2), ('102', 3), ('103', 4))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          3 |       3.60 |
    | Bauru Simples    | 101    | 1.30                |          2 |       2.60 |
    | Bauru com Ovo    | 102    | 1.50                |          3 |       4.50 |
    | Hamburger        | 103    | 1.20                |          4 |       4.80 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |         12 |      15.50 |
    -----------------------------------------------------------------------------

    >>> fechar_conta(('100', 1), ('100', 2), ('101', 2), ('102', 3), ('103', 4), ('104', 5))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          3 |       3.60 |
    | Bauru Simples    | 101    | 1.30                |          2 |       2.60 |
    | Bauru com Ovo    | 102    | 1.50                |          3 |       4.50 |
    | Hamburger        | 103    | 1.20                |          4 |       4.80 |
    | Cheeseburger     | 104    | 1.30                |          5 |       6.50 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |         17 |      22.00 |
    -----------------------------------------------------------------------------
    >>> fechar_conta(('100', 1), ('100', 2), ('101', 2), ('102', 3), ('103', 4), ('105', 6))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          3 |       3.60 |
    | Bauru Simples    | 101    | 1.30                |          2 |       2.60 |
    | Bauru com Ovo    | 102    | 1.50                |          3 |       4.50 |
    | Hamburger        | 103    | 1.20                |          4 |       4.80 |
    | Refrigerante     | 105    | 1.00                |          6 |       6.00 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |         18 |      21.50 |
    -----------------------------------------------------------------------------

"""

def fechar_conta(*itens):
    """Escreva aqui em baixo a sua solução"""

    print("_____________________________________________________________________________")
    print("|                              RESUMO DA CONTA                              |")
    print("|---------------------------------------------------------------------------|")
    print("| Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |")

    quantidade_cq = quantidade_bs = quantidade_bo = quantidade_h = quantidade_c = quantidade_r = 0
    total_cq = total_bs = total_bo = total_h = total_c = total_r = 0
    preco_cq = 1.20
    preco_bs = 1.30
    preco_bo = 1.50
    preco_h = 1.20
    preco_c = 1.30
    preco_r = 1.00

    for cod, quant in itens:
        if cod == '100':
            quantidade_cq += quant
            total_cq = preco_cq * quantidade_cq
        if cod == '101':
            quantidade_bs += quant
            total_bs = preco_bs * quantidade_bs
        if cod == '102':
            quantidade_bo += quant
            total_bo = preco_bo * quantidade_bo
        if cod == '103':
            quantidade_h += quant
            total_h = preco_h * quantidade_h
        if cod == '104':
            quantidade_c += quant
            total_c = preco_c * quantidade_c
        if cod == '105':
            quantidade_r += quant
            total_r = preco_r * quantidade_r

    total_quant_item = quantidade_cq + quantidade_bs + quantidade_bo + quantidade_h + quantidade_c + quantidade_r
    total_compra = total_cq + total_bs + total_bo + total_h + total_c + total_r


    if quantidade_cq > 0:
        print(f"| Cachorro Quente  | 100    | {preco_cq:.2f}                |          {quantidade_cq} |       {total_cq:.2f} |")
    if quantidade_bs > 0:
        print(f"| Bauru Simples    | 101    | {preco_bs:.2f}                |          {quantidade_bs} |       {total_bs:.2f} |")
    if quantidade_bo > 0:
        print(f"| Bauru com Ovo    | 102    | {preco_bo:.2f}                |          {quantidade_bo} |       {total_bo:.2f} |")
    if quantidade_h > 0:
        print(f"| Hamburger        | 103    | {preco_h:.2f}                |          {quantidade_h} |       {total_h:.2f} |")
    if quantidade_c > 0:
        print(f"| Cheeseburger     | 104    | {preco_c:.2f}                |          {quantidade_c} |       {total_c:.2f} |")
    if quantidade_r > 0:
        print(f"| Refrigerante     | 105    | {preco_r:.2f}                |          {quantidade_r} |       {total_r:.2f} |")


    print("|---------------------------------------------------------------------------|")
    print(f"| Total Geral:                                    |{total_quant_item:>11} |{total_compra:>11.2f} |")
    print("-----------------------------------------------------------------------------")
