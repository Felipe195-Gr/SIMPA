from cadastro_produtos import cadastro_produtos
from cadastro_clientes import cadastro_cliente
from cadastro_vendedores import cadastro_vendedores

while True:
    print("Olá, seja bem-vindo ao SIMPA!")
    print("Esse é um sistema de MARKETPLACE de produtos artesanais")
    print(" 1 - Aba de cadastros")
    print(" 5 - Sair")

    escolha = input("Digite o número da opção desejada: ")

    if escolha == "1":

        while True:
            print("Essa é a aba de cadastros")
            print("Cadastro produtos")
            print("Cadastro clientes")
            print("Cadastro vendedores")

            escolha == input("Digite o número da opção desejada: ")
            
            if escolha == "1":
                cadastro_produtos()

            elif escolha == "2":
                cadastro_cliente()
            
            elif escolha == "3":
                cadastro_vendedores()   

    # elif escolha == "5":
    #     print("Obrigado por usar o SIMPA! Até a próxima!")
    #     break
