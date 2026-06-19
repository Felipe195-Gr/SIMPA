import csv
def criar_pedido():
    pedido = {}
    with open("clientes.csv", "r", encoding="utf-8") as arquivo:
        print("Clientes cadastrados:")
        clientes = {}
        for linha in arquivo:
            cpf, nome_cliente, email, cep = linha.strip().split(";")
            clientes[cpf] = {"nome": nome_cliente, "email": email, "cep": cep}
            print(f"CPF: {cpf}, Nome: {nome_cliente}, Email: {email}, CEP: {cep}")
        
        while True:
            cpfcli = input("Digite o CPF do cliente para criar o pedido: ")
            if cpfcli in clientes:
                print(f"Cliente encontrado: {clientes[cpfcli]['nome']}")
                cliente = clientes[cpfcli]
                break
            elif cpfcli.lower() == "sair":
                print("Voltando ao menu principal...")
                return
            else:
                print("CPF não encontrado. Por favor, tente novamente.")
        pedido["id"] = 2
        pedido["cliente"] = cliente
        pedido["entrega"] = cliente["cep"]
        pedido["status"] = "Em andamento"
        pedido["produtos"] = []
        print("Produtos disponíveis:")
        produtos = {}
        with open("cadastro_produtos.csv", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                cod, nome, categoria, preco, estoque, fornecedor = linha.strip().split(";")
                print(f"Código: {cod}, Nome: {nome}, Categoria: {categoria}, Preço: {preco}, Estoque: {estoque}, Fornecedor: {fornecedor}")
                produtos[cod] = {"nome": nome, "categoria": categoria, "preco": preco, "estoque": estoque, "fornecedor": fornecedor}

            while True:
                cod_produto = input("Digite o código do produto para adicionar ao pedido (ou 'sair' para finalizar): ")
                if cod_produto in produtos:
                    if int(produtos[cod_produto]["estoque"]) > 0:
                        pedido["produtos"].append(produtos[cod_produto])
                        produtos[cod_produto]["estoque"] = str(int(produtos[cod_produto]["estoque"]) - 1)
                        print(f"Produto '{produtos[cod_produto]['nome']}' adicionado ao pedido.")
                    else:
                        print("Produto sem estoque disponível.")
                elif cod_produto.lower() == "sair":
                    print("Finalizando o pedido...")
                    break
                else:
                    print("Código de produto não encontrado. Por favor, tente novamente.")
    return pedido

pedido = criar_pedido()
print(pedido)








"""
 pedidos = {
                "1": {
                    "cliente": "João",
                    "entrega": "Rua A, 123",
                    "status": "Em andamento",
                    "produtos": [
                         {001;Vaso de Cerâmica;Decoração;45.90;10;Marcos Silva},
                        "2" : {002;Tapete Artesanal;Decoração;120.00;5;Ana Oliveira}
                        "3" : {003;Caneca Pintada à Mão;Artesanato;35.50;20;João Pereira}
                        "4" : {004;Sabonete Artesanal;Beleza;12.90;30;Maria Santos}
                        "5" : {005;Colar de Miçangas;Acessórios;25.00;15;Carlos Souza}
                        "6" : {006;Quadro Decorativo;Decoração;89.90;8;Fernanda Lima}
                        "7" : {007;Velas Aromáticas;Decoração;18.50;25;Lucas Rocha}
                        "8" : {008;Bolsa de Crochê;Moda;75.00;12;Patrícia Alves}
                        "9" : {009;Chaveiro de Madeira;Artesanato;9.90;40;Rafael Costa}
                        "10" : {010;Cesta de Palha;Artesanato;55.00;7;Juliana Martins}
                        "11" : {011;Porta-retratos de Concreto;Decoração;65.00;10;Mariana Ferreira}
                        "12" : {012;Pote de Cerâmica;Decoração;30.00;20;Ricardo Gomes}
                        "13" : {013;Camiseta Estampada;Moda;40.00;15;Amanda Silva}
                        "14" : {014;Luminária de Madeira;Decoração;120.00;5;Bruno Santos}
                        "15" : {015;Caderno Artesanal;Papelaria;25.00;30;Carla Mendes}

                    ]
                }
 }

pedidos["1"]["cliente"] 
      pedidos["1"]["cliente"]["produtos"]
pedidos[numero_selecionado_digitado]["status"] 

print(pedidos[numero_selecionado_digitado]["produtos"])
produto_para_remover = 1
pedidos[numero_selecionado_digitado]["produtos"].pop(produto_para_remover)

"""
