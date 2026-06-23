import requests
import csv
import os
from datetime import datetime
from calculos import *
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
    cpf = input("Digite o CPF do vendedor: ")
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

# ===================== CSV DE PEDIDOS =====================

    produtos_texto = "|".join(
    [f"{p['nome']}({p['preco']}:{p['fornecedor']})" for p in pedido["produtos"]]   
    )

    with open("pedidos.csv", "a", encoding="utf-8") as arquivo:
        arquivo.write(
            f"{pedido['id']};"
            f"{pedido['cliente']['nome']};"
            f"{pedido['cliente']['email']};"
            f"{pedido['entrega']};"
            f"{pedido['status']};"
            f"{valor_total:.2f};"
            f"{frete:.2f};"
            f"{total_final:.2f};"
            f"{produtos_texto}\n"
        )

    print("\nPedido salvo em: pedidos.csv")
    atualizar_estoque(pedido["produtos"])
    return pedido

def atualizar_estoque(produtos_vendidos):
    produtos = []

    # ler arquivo atual
    with open("cadastro_produtos.csv", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            cod, nome, categoria, preco, estoque, fornecedor = linha.strip().split(";")

            produtos.append({
                "cod": cod,
                "nome": nome,
                "categoria": categoria,
                "preco": preco,
                "estoque": int(estoque),
                "fornecedor": fornecedor
            })

    # reduzir estoque
    for vendido in produtos_vendidos:
        for p in produtos:
            if p["nome"] == vendido["nome"]:
                if p["estoque"] > 0:
                    p["estoque"] -= 1

    # reescrever arquivo
    with open("cadastro_produtos.csv", "w", encoding="utf-8") as arquivo:
        for p in produtos:
            arquivo.write(
                f"{p['cod']};{p['nome']};{p['categoria']};{p['preco']};{p['estoque']};{p['fornecedor']}\n"
            )

def relatorio_total_vendido():
    total_vendido = 0

    with open("pedidos.csv", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(";")

            if len(dados) < 8:
                continue  # ignora linha inválida

            total = float(dados[7])  # coluna "total_final"
            total_vendido += total

    print(f"Total vendido: R$ {total_vendido:.2f}")
    return total_vendido

def comissao_total_plataforma():
    total_comissao = 0

    with open("pedidos.csv", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(";")

            if len(dados) < 9:
                continue

            produtos_texto = dados[8]  # coluna produtos

            if produtos_texto.strip() == "":
                continue

            produtos = produtos_texto.split("|")

            for p in produtos:
                try:
                    # formato: Nome(preco)
                    preco = float(p.split("(")[1].replace(")", ""))
                    total_comissao += calcular_comissao(preco)
                except:
                    continue

    print(f"Comissão total: R$ {total_comissao:.2f}")
    return total_comissao

def relatorio_vendas_por_vendedor():
    vendas = {}

    with open("pedidos.csv", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(";")

            if len(dados) < 9:
                continue

            produtos = dados[8].split("|")

            for p in produtos:
                try:
                    nome = p.split("(")[0]
                    preco_vendedor = p.split("(")[1].replace(")", "")
                    preco, vendedor = preco_vendedor.split(":")

                    preco = float(preco)

                    if vendedor not in vendas:
                        vendas[vendedor] = 0

                    vendas[vendedor] += preco

                except:
                    continue

    for vendedor, total in vendas.items():
        print(f"{vendedor}: R$ {total:.2f}")

def produto_mais_vendido():
    vendas = {}

    with open("pedidos.csv", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(";")

            if len(dados) < 9:
                continue

            produtos = dados[8].split("|")

            for p in produtos:
                try:
                    nome = p.split("(")[0].strip()

                    if nome not in vendas:
                        vendas[nome] = 0

                    vendas[nome] += 1

                except:
                    continue

    if not vendas:
        print("Nenhuma venda registrada.")
        return

    mais_vendido = max(vendas, key=vendas.get)

    print(f"Produto mais vendido: {mais_vendido} ({vendas[mais_vendido]} vendas)")
    return mais_vendido


def relatorio_estoque():
    produtos = []

    with open("cadastro_produtos.csv", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            cod, nome, cat, preco, estoque, forn = linha.strip().split(";")

            produtos.append({
                "cod": cod,
                "nome": nome,
                "estoque": int(estoque)
            })

    produtos.sort(key=lambda x: x["estoque"])

    print("\n=== ESTOQUE (MENOR PARA MAIOR) ===\n")

    for p in produtos:
        print(f"{p['nome']} - estoque: {p['estoque']}")