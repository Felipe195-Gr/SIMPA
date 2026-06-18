def cadastro_cliente():
    print("Cadastro de Clientes")
    nome = input("Digite o nome do cliente: ")
    email = input("Digite o email do cliente: ")
    endereco = input("Digite o endereço do cliente")

    with open ('C:\\Users\\felip\\OneDrive\\Documentos\\SIMPA\\clientes.csv', 'a', encoding='utf-8') as arquivo:
        arquivo.write(f"{nome},{email},{endereco}\n")
