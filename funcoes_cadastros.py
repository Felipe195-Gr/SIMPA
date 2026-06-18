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

    with open(f'cadastro_produtos.csv', 'a') as arquivo:
        arquivo.write(f"{codigo};{nome};{categoria};{preco};{estoque};{vendedor}\n")    
        print("Produto cadastrado com sucesso!")

#função que cadastra os clientes
def cadastro_cliente():
    print("Cadastro de Clientes")
    nome = input("Digite o nome do cliente: ")
    email = input("Digite o email do cliente: ")
    cep = input("Digite o endereço do cliente: ")

    with open ('clientes.csv', 'a', encoding='utf-8') as arquivo:
        arquivo.write(f"{nome};{email};{cep}\n")

#função que cadastra os vendedores
def cadastro_vendedores():
    nome = input("Qual é o nome do vendedor: ")
    telefone = input("Qual é o telefone do vendedor(49)xxxxx-xxxx: ")
    cep = input("Qual é o CEP do vendedor (xxxxx-xxx): ")

    with open('vendedores.csv', 'a', encoding='utf-8') as arquivo:
        arquivo.write(f"{nome};{telefone};{cep}")