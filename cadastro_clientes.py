def cadastro_cliente(nome, email, CEP):
    print("Cadastro de Clientes")
    nome = input("Digite o nome do cliente: ")
    email = input("Digite o email do cliente: ")
    CEP = input("Digite o CEP do cliente: ")
    
    with open("C:\\Users\\felip\\OneDrive\\Documentos\\SIMPA\\clientes.csv", "a") as arquivo:
        arquivo.write(f"{nome},{email},{CEP}\n")