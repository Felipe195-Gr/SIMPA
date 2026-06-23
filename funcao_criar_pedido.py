# import csv
# import os
# from datetime import datetime
# from calculos import calcular_total, calcular_frete


# def criar_pedido():
#     pedido = {}

#     # ===================== CLIENTES =====================
#     with open("clientes.csv", "r", encoding="utf-8") as arquivo:
#         print("Clientes cadastrados:")
#         clientes = {}

#         for linha in arquivo:
#             cpf, nome_cliente, email, cep = linha.strip().split(";")
#             clientes[cpf] = {
#                 "nome": nome_cliente,
#                 "email": email,
#                 "cep": cep
#             }
#             print(f"CPF: {cpf}, Nome: {nome_cliente}, Email: {email}, CEP: {cep}")

#     # selecionar cliente
#     while True:
#         cpfcli = input("Digite o CPF do cliente para criar o pedido (ou 'sair'): ")

#         if cpfcli.lower() == "sair":
#             print("Voltando ao menu principal...")
#             return

#         if cpfcli in clientes:
#             print(f"Cliente encontrado: {clientes[cpfcli]['nome']}")
#             cliente = clientes[cpfcli]
#             break
#         else:
#             print("CPF não encontrado. Tente novamente.")

#     # ===================== PEDIDO =====================
#     pedido["id"] = 2
#     pedido["cliente"] = cliente
#     pedido["entrega"] = cliente["cep"]
#     pedido["status"] = "Em andamento"
#     pedido["produtos"] = []

#     # ===================== PRODUTOS =====================
#     print("\nProdutos disponíveis:")
#     produtos = {}

#     with open("cadastro_produtos.csv", "r", encoding="utf-8") as arquivo:
#         for linha in arquivo:
#             cod, nome, categoria, preco, estoque, fornecedor = linha.strip().split(";")

#             produtos[cod] = {
#                 "nome": nome,
#                 "categoria": categoria,
#                 "preco": float(preco),
#                 "estoque": int(estoque),
#                 "fornecedor": fornecedor
#             }

#             print(f"Código: {cod}, Nome: {nome}, Preço: {preco}, Estoque: {estoque}")

#     # adicionar produtos
#     while True:
#         cod_produto = input("Digite o código do produto (ou 'sair'): ")

#         if cod_produto.lower() == "sair":
#             print("Finalizando o pedido...")
#             break

#         if cod_produto in produtos:
#             produto = produtos[cod_produto]

#             if produto["estoque"] > 0:
#                 pedido["produtos"].append(produto)
#                 produtos[cod_produto]["estoque"] -= 1
#                 print(f"Produto '{produto['nome']}' adicionado ao pedido.")
#             else:
#                 print("Produto sem estoque.")
#         else:
#             print("Código de produto não encontrado.")

#     # ===================== CÁLCULOS =====================
#     valor_total = calcular_total(pedido["produtos"])
#     frete = calcular_frete(valor_total)
#     total_final = valor_total + frete

#     # ===================== ARQUIVO =====================
#     pasta_downloads = os.path.join(os.path.expanduser("~"), "Downloads")

#     nome_arquivo = os.path.join(
#         pasta_downloads,
#         f"pedido_{cpfcli}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
#     )

#     with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
#         arquivo.write("=== PEDIDO SIMPA ===\n\n")
#         arquivo.write(f"ID: {pedido['id']}\n")
#         arquivo.write(f"Cliente: {pedido['cliente']['nome']}\n")
#         arquivo.write(f"Email: {pedido['cliente']['email']}\n")
#         arquivo.write(f"CEP de entrega: {pedido['entrega']}\n")
#         arquivo.write(f"Status: {pedido['status']}\n\n")
#         arquivo.write("\n")
#         arquivo.write(f"Valor dos produtos: R$ {valor_total:.2f}\n")
#         arquivo.write(f"Frete: R$ {frete:.2f}\n")
#         arquivo.write(f"Total final: R$ {total_final:.2f}\n")

#         arquivo.write("PRODUTOS:\n")

#         for produto in pedido["produtos"]:
#             arquivo.write(
#                 f"- {produto['nome']} | "
#                 f"Categoria: {produto['categoria']} | "
#                 f"Preço: R$ {produto['preco']:.2f} | "
#                 f"Fornecedor: {produto['fornecedor']}\n"
#             )

        

#     print(f"\nPedido salvo em:\n{nome_arquivo}")

#     return pedido