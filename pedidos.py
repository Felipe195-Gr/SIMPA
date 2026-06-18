produto = input("Digite o nome do produto: ")


def pedidos():
    while True:
        produto = input("Digite o nome do produto: ")
        with open('C:\\Users\\uriel\\OneDrive\\Documentos\\Programação\\SIMPA\\cadastro_produtos.csv', 'r') as arquivo: 
            arquivo.read()
            for linha in arquivo:
                linha = linha.strip()
                dados = linha.split(",")
                codigo = dados[0]
                nome_produto = dados[1]
            print(f"produto pesquisado: {produto}, {codigo}, {nome_produto}")
            
