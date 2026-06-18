produto = input("Digite o nome do produto: ")


def pedidos():
    while True:
        produto = input("Digite o nome do produto: ")
        with open('C:\\Users\\uriel\\OneDrive\\Documentos\\Programação\\SIMPA\\cadastro_produtos.csv', 'r') as arquivo:
            arquivo.read()
            print(f"{produto}")
            
