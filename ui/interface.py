from utils.cardapio import carregar_cardapio, caminho_cardapio

def visualizar_menu():
    print()
    print("-------- OPÇÕES DISPONÍVEIS --------")
    print()
    print("1. Ver Cardápio")
    print("2. Incluir algo")
    print("3. Excluir algo")
    print("6. Limpar Cardápio")
    print("7. Encerrar e salvar o cardápio")

estoque = {
    "entradas": [],
    "pratos_principais": [],
    "bebidas": [],
    "sobremesas": []
}

def ver_cardapio():
    if all(not estoque[categoria] for categoria in estoque):
        print("Cardápio vazio no momento.")
        return

    print("\nEntradas disponíveis:")
    for item in estoque["entradas"]:
        print(f"• {item['nome']} - R${item['preco']:.2f}")

    print("\nPratos principais disponíveis:")
    for item in estoque["pratos_principais"]:
        print(f"• {item['nome']} - R${item['preco']:.2f}")

    print("\nSobremesas disponíveis:")
    for item in estoque["sobremesas"]:
        print(f"• {item['nome']} - R${item['preco']:.2f}")

    print("\nBebidas disponíveis:")
    for item in estoque["bebidas"]:
        print(f"• {item['nome']} - R${item['preco']:.2f}")

def incluir_entrada():
    nome = input("Nome da entrada: ")
    try:
        preco = float(input("Preço da entrada: R$ ").replace(",", "."))
        estoque["entradas"].append({"nome": nome, "preco": preco})
        print(f"{nome} foi incluído no cardápio.")
    except ValueError:
        print("Preço inválido. Use apenas números.")

def excluir_entrada():
    nome = input("Nome da entrada a remover: ")
    for item in estoque["entradas"]:
        if item["nome"] == nome:
            estoque["entradas"].remove(item)
            print(f"{nome} foi removido.")
            return
    print(f"{nome} não foi encontrado.")

def incluir_pratos_principais():
    nome = input("Nome do prato principal: ")
    try:
        preco = float(input("Preço do prato: R$ ").replace(",", "."))
        estoque["pratos_principais"].append({"nome": nome, "preco": preco})
        print(f"{nome} foi incluído no cardápio.")
    except ValueError:
        print("Preço inválido. Use apenas números.")

def excluir_pratos_principais():
    nome = input("Nome do prato principal a remover: ")
    for item in estoque["pratos_principais"]:
        if item["nome"] == nome:
            estoque["pratos_principais"].remove(item)
            print(f"{nome} foi removido.")
            return
    print(f"{nome} não foi encontrado.")

def incluir_sobremesa():
    nome = input("Nome da sobremesa: ")
    try:
        preco = float(input("Preço da sobremesa: R$ ").replace(",", "."))
        estoque["sobremesas"].append({"nome": nome, "preco": preco})
        print(f"{nome} foi incluído no cardápio.")
    except ValueError:
        print("Preço inválido. Use apenas números.")

def excluir_sobremesa():
    nome = input("Nome da sobremesa a remover: ")
    for item in estoque["sobremesas"]:
        if item["nome"] == nome:
            estoque["sobremesas"].remove(item)
            print(f"{nome} foi removida.")
            return
    print(f"{nome} não foi encontrada.")

def incluir_bebida():
    nome = input("Nome da bebida: ")
    try:
        preco = float(input("Preço da bebida: R$ ").replace(",", "."))
        estoque["bebidas"].append({"nome": nome, "preco": preco})
        print(f"{nome} foi adicionada ao cardápio.")
    except ValueError:
        print("Preço inválido. Use apenas números.")

def excluir_bebida():
    nome = input("Nome da bebida a remover: ")
    for item in estoque["bebidas"]:
        if item["nome"] == nome:
            estoque["bebidas"].remove(item)
            print(f"{nome} foi removida.")
            return
    print(f"{nome} não foi encontrada.")

def limpar_cardapio():
    for categoria in estoque:
        estoque[categoria].clear()
    print("Cardápio foi limpo com sucesso.")

while True:
    visualizar_menu()
    escolha = input("Selecione uma das opções: ")

    if escolha == "1":
        ver_cardapio()
    elif escolha == "2":
        tipo = input("Deseja incluir (1) Entradas, (2) Pratos principais, (3) Sobremesas, (4) Bebidas: ")
        if tipo == "1":
            incluir_entrada()
        elif tipo == "2":
            incluir_pratos_principais()
        elif tipo == "3":
            incluir_sobremesa()
        elif tipo == "4":
            incluir_bebida()
        else:
            print("Opção inválida.")
    elif escolha == "3":
        tipo = input("Deseja excluir (1) Entradas, (2) Pratos principais, (3) Sobremesas, (4) Bebidas: ")
        if tipo == "1":
            excluir_entrada()
        elif tipo == "2":
            excluir_pratos_principais()
        elif tipo == "3":
            excluir_sobremesa()
        elif tipo == "4":
            excluir_bebida()
        else:
            print("Opção inválida.")
    elif escolha == "6":
        limpar_cardapio()
    elif escolha == "7":
        print("Fechando cardápio.")
        break
    else:
        print("Escolha inválida. Tente novamente.")
