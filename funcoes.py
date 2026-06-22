import requests
import csv
from funcao_criar_pedido import *

#função que cadastra os produtos

def cadastro_produtos():
    print("Cadastro de Produtos")
    codigo = input("Digite o código do produto: ")
    nome = input("Digite o nome do produto: ")
    categoria = input("Digite a categoria do produto: ")
    preco = float(input("Digite o preço do produto: "))
    estoque = int(input("Digite a quantidade em estoque: "))
    print("\nVendedores cadastrados:")

    with open("vendedores.csv", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(";")
            print(dados[0])

    vendedor = input("Digite o nome do vendedor: ")

    with open(f'cadastro_produtos.csv', 'a', encoding="utf-8") as arquivo:
        arquivo.write(f"{codigo};{nome};{categoria};{preco};{estoque};{vendedor}\n")    
        print("Produto cadastrado com sucesso!")
    return preco
#função que cadastra os clientes
def cadastro_cliente():
    print("Cadastro de Clientes")
    cpf = input("Digite o CPF do cliente: ")
    nome = input("Digite o nome do cliente: ")
    email = input("Digite o email do cliente: ")
    cep = input("Digite o endereço do cliente: ")


    with open ('clientes.csv', 'a', encoding='utf-8') as arquivo:
        arquivo.write(f"{cpf};{nome};{email};{cep}\n")

#função que cadastra os vendedores
def cadastro_vendedores():
    cpf = input("Digite o CPF do vendedor")
    nome = input("Qual é o nome do vendedor: ")
    telefone = input("Qual é o telefone do vendedor(49)xxxxx-xxxx: ")
    cep = input("Qual é o CEP do vendedor (xxxxx-xxx): ")
    
    with open('vendedores.csv', 'a', encoding='utf-8') as arquivo:
        arquivo.write(f"{cpf};{nome};{telefone};{cep}\n")

def consulta():
    while True:
        produto = input("Digite o nome do produto: ")
        with open('cadastro_produtos.csv', 'r', encoding="utf-8") as arquivo: 
            for linha in arquivo:
                linha = linha.strip()
                dados = linha.split(";")
                codigo = dados[0]
                nome_produto = dados[1]
                categoria = dados[2]
                preco = dados[3]
                estoque = dados[4]
                vendedor = dados[5]
                if produto == nome_produto:
                    print(f"produto pesquisado: {produto},ID:{codigo}, {nome_produto}, {categoria}, R${preco}, {estoque}, {vendedor}")
        break
    
# def relatorio_total_vendido(pedidos):
#     total_vendido = 0
#     for pedido in pedidos:
#         total_vendido += calcular_total(pedido)
#     total = relatorio_total_vendido(pedidos)
#     print(f"Total vendido: R$ {total:.2f}")
#     return total_vendido

# def comissao_total_plataforma(pedidos):
#     comissao_total = 0
#     for pedido in pedidos:
#         comissao_total += pedido['comissao']
#     return comissao_total

def consultar_Cep():
    with open("clientes.csv", "r", encoding="utf-8") as arquivo:
        print("Clientes cadastrados:")
        clientes = {}

        for linha in arquivo:
            cpf, nome_cliente, email, cep = linha.strip().split(";")
            clientes[cpf] = {
                "nome": nome_cliente,
                "email": email,
                "cep": cep
            }
            print(f"CPF: {cpf}, Nome: {nome_cliente}, Email: {email}, CEP: {cep}")

    cep = input("Digite o CEP:")
    url = f"https://viacep.com.br/ws/{cep}/json/"

    response = requests.get(url)
    dados = response.json()

    print(f"CEP: {dados['cep']}")
    print(f"Endereço: {dados['logradouro']}")
    print(f"Bairro: {dados['bairro']}")
    print(f"Cidade: {dados['localidade']}")
    print(f"Estado: {dados['uf']}")

import csv
import os
from datetime import datetime
from calculos import calcular_total, calcular_frete


def criar_pedido():
    pedido = {}

    # ===================== CLIENTES =====================
    with open("clientes.csv", "r", encoding="utf-8") as arquivo:
        print("Clientes cadastrados:")
        clientes = {}

        for linha in arquivo:
            cpf, nome_cliente, email, cep = linha.strip().split(";")
            clientes[cpf] = {
                "nome": nome_cliente,
                "email": email,
                "cep": cep
            }
            print(f"CPF: {cpf}, Nome: {nome_cliente}, Email: {email}, CEP: {cep}")

    # selecionar cliente
    while True:
        cpfcli = input("Digite o CPF do cliente para criar o pedido (ou 'sair'): ")

        if cpfcli.lower() == "sair":
            print("Voltando ao menu principal...")
            return

        if cpfcli in clientes:
            print(f"Cliente encontrado: {clientes[cpfcli]['nome']}")
            cliente = clientes[cpfcli]
            break
        else:
            print("CPF não encontrado. Tente novamente.")

    # ===================== PEDIDO =====================
    pedido["id"] = 2
    pedido["cliente"] = cliente
    pedido["entrega"] = cliente["cep"]
    pedido["status"] = "Em andamento"
    pedido["produtos"] = []

    # ===================== PRODUTOS =====================
    print("\nProdutos disponíveis:")
    produtos = {}

    with open("cadastro_produtos.csv", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            cod, nome, categoria, preco, estoque, fornecedor = linha.strip().split(";")

            produtos[cod] = {
                "nome": nome,
                "categoria": categoria,
                "preco": float(preco),
                "estoque": int(estoque),
                "fornecedor": fornecedor
            }

            print(f"Código: {cod}, Nome: {nome}, Preço: {preco}, Estoque: {estoque}")

    # adicionar produtos
    while True:
        cod_produto = input("Digite o código do produto (ou 'sair'): ")

        if cod_produto.lower() == "sair":
            print("Finalizando o pedido...")
            break

        if cod_produto in produtos:
            produto = produtos[cod_produto]

            if produto["estoque"] > 0:
                pedido["produtos"].append(produto)
                produtos[cod_produto]["estoque"] -= 1
                print(f"Produto '{produto['nome']}' adicionado ao pedido.")
            else:
                print("Produto sem estoque.")
        else:
            print("Código de produto não encontrado.")

    # ===================== CÁLCULOS =====================
    valor_total = calcular_total(pedido["produtos"])
    frete = calcular_frete(valor_total)
    total_final = valor_total + frete

    # ===================== ARQUIVO =====================
    pasta_downloads = os.path.join(os.path.expanduser("~"), "Downloads")

    nome_arquivo = os.path.join(
        pasta_downloads,
        f"pedido_{cpfcli}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    )

    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write("=== PEDIDO SIMPA ===\n\n")
        arquivo.write(f"ID: {pedido['id']}\n")
        arquivo.write(f"Cliente: {pedido['cliente']['nome']}\n")
        arquivo.write(f"Email: {pedido['cliente']['email']}\n")
        arquivo.write(f"CEP de entrega: {pedido['entrega']}\n")
        arquivo.write(f"Status: {pedido['status']}\n\n")
        arquivo.write("\n")
        arquivo.write(f"Valor dos produtos: R$ {valor_total:.2f}\n")
        arquivo.write(f"Frete: R$ {frete:.2f}\n")
        arquivo.write(f"Total final: R$ {total_final:.2f}\n")

        arquivo.write("PRODUTOS:\n")

        for produto in pedido["produtos"]:
            arquivo.write(
                f"- {produto['nome']} | "
                f"Categoria: {produto['categoria']} | "
                f"Preço: R$ {produto['preco']:.2f} | "
                f"Fornecedor: {produto['fornecedor']}\n"
            )

        

    print(f"\nPedido salvo em:\n{nome_arquivo}")

    return pedido
