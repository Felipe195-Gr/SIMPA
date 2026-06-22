from funcoes import *
from funcao_criar_pedido import criar_pedido
while True:
    print("Olá, seja bem-vindo ao SIMPA!")
    print("Esse é um sistema de MARKETPLACE de produtos artesanais")
    print(" 1 - Aba de cadastros")
    print(" 2 - Criar pedidos ou consultar produtos e CEP")
    print(" 3 - Gerar relatório")
    print(" 4 - Comissão total")
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
        
        while True:
            print(" 1 - Consultar produtos")
            print(" 2 - Criar pedidos")
            print(" 3 - Consultar Cep do cliente")
            print(" 4 - Sair")

            escolha_pedidos = input("Digite o número da opção desejada: ")

            if escolha_pedidos == "1":
                consulta()

            elif escolha_pedidos == "2":
                criar_pedido()
            
            elif escolha_pedidos == "3":
                consultar_Cep()

            elif escolha_pedidos == "4":
                break
    elif escolha == "3":
        relatorio_total_vendido()

    elif escolha == "4":
        comissao_total_plataforma()
        
    elif escolha == "5":
        print("Obrigado por usar o SIMPA! Até a próxima!")
        break

