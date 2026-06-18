produto = input("Digite o nome do produto: ")


def pedidos():
    while True:
        print("-------Menu de pedidos-------")
        with open('C:\\Users\\uriel\\OneDrive\\Documentos\\Programação\\SIMPA\\cadastro_produtos.csv', 'r') as arquivo:
            arquivo.read()
            print("1 - Mostrar produtos")
            
produto = input("Digite o nome do produto: ")