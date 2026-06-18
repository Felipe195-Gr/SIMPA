from funcoes_cadastros import cadastro_produtos
from funcoes_cadastros import cadastro_cliente
from funcoes_cadastros import cadastro_vendedores
from pedidos import pedidos

while True:
    print("Olá, seja bem-vindo ao SIMPA!")
    print("Esse é um sistema de MARKETPLACE de produtos artesanais")
    print(" 1 - Aba de cadastros")
    print(" 2 - Pedidos")
    print(" 5 - Sair")

    escolha = input("Digite o número da opção desejada: ")

    if escolha == "1":

        while True:
            print("Essa é a aba de cadastros")
            print(" 1 - Cadastro vendedores")
            print(" 2 - Cadastro clientes")
            print(" 3 - Cadastro produtos")
            print(" 4 - Sair")

            escolha_cadastros = input("Digite o número da opção desejada: ")
            
            if escolha_cadastros == "1":
                cadastro_vendedores()

            elif escolha_cadastros == "2":
                cadastro_cliente()
            
            elif escolha_cadastros == "3":
                cadastro_produtos()   

            elif escolha_cadastros == "4":
                print("Saindo do menu de cadastros")
                break
    
    elif escolha == "2":
        pedidos()

    elif escolha == "5":
        print("Obrigado por usar o SIMPA! Até a próxima!")
        break

