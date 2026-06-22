import requests
import csv

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
        arquivo.write(f"{cpf};{nome};{telefone};{cep}")

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
    
def relatorio_total_vendido(pedidos):
    from calculos import calcular_total
    total_vendido = 0
    for pedido in pedidos:
        total_vendido += calcular_total(pedido)
    total = relatorio_total_vendido(pedidos)
    print(f"Total vendido: R$ {total:.2f}")
    return total_vendido

def consultar_Cep():
    with open("clientes.csv", "r", encoding="utf-8") as arquivo:
        print("Clientes cadastrados:")
        clientes = {}

    cep = input("Digite o CEP:")
    url = f"https://viacep.com.br/ws/{cep}/json/"

    response = requests.get(url)
    dados = response.json()

    print(f"CEP: {dados['cep']}")
    print(f"Endereço: {dados['logradouro']}")
    print(f"Bairro: {dados['bairro']}")
    print(f"Cidade: {dados['localidade']}")
    print(f"Estado: {dados['uf']}")
