def visualizar_menu():
    print(" OPÇÕES DISPONÍVEIS ")
    print("1. Ver Cardápio")
    print("2. Incluir algo")
    print("3. Excluir algo")
    print("6. Limpar Cardápio")
    print("7. Encerrar e salvar o cardápio")

estoque = {
    "pratos": [],
    "drinks": []
}

def ver_cardapio():
    print("\n CARDÁPIO ATUAL ")
    if not estoque["pratos"] and not estoque["drinks"]:
        print("Cardápio vazio no momento.")
    else:
        print("Pratos disponíveis:")
        for item in estoque["pratos"]:
            print(f"• {item['nome']} - R${item['preco']:.2f}")
        print("Bebidas disponíveis:")
        for item in estoque["drinks"]:
            print(f"• {item['nome']} - R${item['preco']:.2f}")

def incluir_prato():
    nome = input("Nome do prato: ")
    try:
        preco = float(input("Preço do prato: R$ ").replace(",", "."))
        estoque["pratos"].append({"nome": nome, "preco": preco})
        print(f"{nome} foi incluído no cardápio.")
    except ValueError:
        print("Preço inválido. Use apenas números.")

def excluir_prato():
    nome = input("Nome do prato a remover: ")
    for item in estoque["pratos"]:
        if item["nome"] == nome:
            estoque["pratos"].remove(item)
            print(f"{nome} foi removido.")
            return
    print(f"{nome} não foi encontrado.")

def incluir_bebida():
    nome = input("Nome da bebida: ")
    try:
        preco = float(input("Preço da bebida: R$ ").replace(",", "."))
        estoque["drinks"].append({"nome": nome, "preco": preco})
        print(f"{nome} foi adicionada ao cardápio.")
    except ValueError:
        print("Preço inválido. Use apenas números.")

def excluir_bebida():
    nome = input("Nome da bebida a remover: ")
    for item in estoque["drinks"]:
        if item["nome"] == nome:
            estoque["drinks"].remove(item)
            print(f"{nome} foi removida.")
            return
    print(f"{nome} não foi encontrada.")

def limpar_cardapio():
    estoque["pratos"].clear()
    estoque["drinks"].clear()
    print("Cardápio foi limpo com sucesso.")
