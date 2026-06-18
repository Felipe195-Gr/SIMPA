def criar_pedido():
    while True:
        pedido = input("Digite o pedido que deseja criar: ")
        with open('pedidos.csv', 'a', encoding='utf-8') as arquivo:
            arquivo.write(f"{pedido}\n")
            print("Pedido criado com sucesso!")