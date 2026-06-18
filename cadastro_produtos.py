def cadastro_produtos():
    print("Cadastro de Produtos")
    nome_produto = input("Digite o nome do produto: ")
    descricao_produto = input("Digite a descrição do produto: ")
    preco_produto = float(input("Digite o preço do produto: "))
    with open(f'C:\\Users\\uriel61918066\\Documents\\SIMPA\\cadastro_produtos.csv', 'a') as arquivo:
        arquivo.write(f"{nome_produto};{descricao_produto}; R${preco_produto:.2f}\n")
    print("Produto cadastrado com sucesso!")