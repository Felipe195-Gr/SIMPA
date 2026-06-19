import cadastro_produtos.csv
def criar_pedido():
    with open("cadastro_produtos.csv", "r", encoding="utf-8") as arquivo:
        leitor = cadastro_produtos.csv.DictReader(arquivo)

    for linha in leitor:
        print(linha)
"""
 pedidos = {
                "1": {
                    "cliente": "João",
                    "entrega": "Rua A, 123",
                    "status": "Em andamento",
                    "produtos": [
                        "1" : {015;Escultura em Madeira;Artesanato;150.00;3;Thiago Ribeiro},
                        "2" : {015;Escultura em Madeira;Artesanato;150.00;3;Thiago Ribeiro1}
                        "3" : {015;Escultura em Madeira;Artesanato;150.00;3;Thiago Ribeiro2}
                        "4" : {015;Escultura em Madeira;Artesanato;150.00;3;Thiago Ribeiro3}
                        "5" : {015;Escultura em Madeira;Artesanato;150.00;3;Thiago Ribeiro4}
                        "6" : {015;Escultura em Madeira;Artesanato;150.00;3;Thiago Ribeiro5}
                        "7" : {015;Escultura em Madeira;Artesanato;150.00;3;Thiago Ribeiro6}
                        "8" : {015;Escultura em Madeira;Artesanato;150.00;3;Thiago Ribeiro7}
                        "9" : {015;Escultura em Madeira;Artesanato;150.00;3;Thiago Ribeiro8}
                        "10" : {015;Escultura em Madeira;Artesanato;150.00;3;Thiago Ribeiro9}
                        "

                    ]
                }
 }

pedidos["1"]["cliente"] 
      pedidos["1"]["cliente"]["produtos"]
pedidos[numero_selecionado_digitado]["status"] 

print(pedidos[numero_selecionado_digitado]["produtos"])
produto_para_remover = 1
pedidos[numero_selecionado_digitado]["produtos"].pop(produto_para_remover)

"""
