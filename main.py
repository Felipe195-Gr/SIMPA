from cadastro_produtos import cadastrar_produto
from cadastro_clientes import cadastrar_cliente

while True:
    print("Olá, seja bem-vindo ao SIMPA!")
    print("Esse é um sistema de MARKETPLACE de produtos artesanais")
    print(" 1 - Cadastrar produto")
    print(" 2 - Cadastrar clientes")
    print(" 3 - Cadastrar vendedores")
    print(" 4 - Consultar endereço")
    print(" 5 - Sair")

    escolha = input("Digite o número da opção desejada: ")

    if escolha == 1:
        cadastrar_produto()

    elif escolha == 2:
        cadastrar_cliente