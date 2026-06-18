def calcular_comissao(preco_produto):
    if preco_produto <= 50:
        comissao = preco_produto * 0.05
    elif preco_produto >= 50.01 and preco_produto <= 200:
        comissao = preco_produto * 0.08
    else:
        comissao = preco_produto * 0.12
    
    return comissao

def calcular_total(preco_produto, frete):
    if preco_produto > 250.00:
        frete = 0
    elif preco_produto <= 250.00:
        frete = 15.00
        total = preco_produto + frete
    return total