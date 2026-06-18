def pedidos():
    while True:
        produto = input("Digite o nome do produto: ")
        with open('C:\\Users\\uriel\\OneDrive\\Documentos\\Programação\\SIMPA\\cadastro_produtos.csv', 'r', encoding="utf-8") as arquivo: 
            for linha in arquivo:
                linha = linha.strip()
                dados = linha.split(";")
                codigo = dados[0]
                nome_produto = dados[1]
                categoria = dados[2]
                preco = dados[3]
                estoque = dados[4]
                vendedor = dados[5]
                if produto == nome_produto:
                    print(f"produto pesquisado: {produto}, {codigo}, {nome_produto}, {categoria}, {preco}, {estoque}, {vendedor}")
        break

pedidos()
            
