def cadastro_vendedores():
    nome = input("Qual é o nome do vendedor: ")
    telefone = input("Qual é o telefone do vendedor(49)xxxxx-xxxx: ")
    cep = input("Qual é o CEP do vendedor (xxxxx-xxx): ")

    with open('vendedores.csv', 'a', encoding='utf-8') as arquivo:
        arquivo.write(f"{nome};{telefone};{cep}")