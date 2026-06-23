def calcular_comissao(preco):
    if preco <= 50:
        return preco * 0.05
    elif preco <= 200:
        return preco * 0.08
    else:
        return preco * 0.12


def calcular_frete(valor_total):
    if valor_total > 250:
        return 0
    else:
        return 15


def calcular_total(produtos):
    return sum(float(produto["preco"]) for produto in produtos)