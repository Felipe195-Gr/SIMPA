def cadastro_produtos():
    print("Cadastro de Produtos")
    codigo = input("Digite o código do produto: ")
    nome = input("Digite o nome do produto: ")
    categoria = input("Digite a categoria do produto: ")
    preco = float(input("Digite o preço do produto: "))
    estoque = int(input("Digite a quantidade em estoque: "))
    vendedor = input("Digite o nome do vendedor: ")

    with open(f'cadastro_produtos.csv', 'a') as arquivo:
        arquivo.write(f"{codigo};{nome};{categoria};{preco};{estoque};{vendedor}")
        print("Produto cadastrado com sucesso!")