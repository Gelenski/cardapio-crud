def visualizar_menu():
    print("\n-------- OPÇÕES DISPONÍVEIS --------\n")
    print("1. Ver Cardápio")
    print("2. Incluir algo")
    print("3. Excluir algo")
    print("6. Limpar Cardápio")
    print("7. Encerrar e salvar o cardápio")

def ver_cardapio(cardapio):
    if not cardapio:
        print("Cardápio vazio no momento.")
        return
    for categoria in cardapio:
        print(f"\n{categoria['categoria'].capitalize()}:")
        for item in categoria['itens']:
            print(f"• {item['nome']} - R${item['preco']:.2f}")

def incluir_item(cardapio, tipo):
    nome = input(f"Nome do {tipo}: ")
    try:
        preco = float(input(f"Preço do {tipo}: R$ ").replace(",", "."))
        for categoria in cardapio:
            if categoria['categoria'].lower() == tipo.lower():
                categoria['itens'].append({"nome": nome, "preco": preco})
                break
        else:
            cardapio.append({"categoria": tipo, "itens": [{"nome": nome, "preco": preco}]})
        print(f"{nome} foi incluído no cardápio.")
    except ValueError:
        print("Preço inválido. Use apenas números.")

def excluir_item(cardapio, tipo):
    nome = input(f"Nome do {tipo} a remover: ")
    for categoria in cardapio:
        if categoria['categoria'].lower() == tipo.lower():
            for item in categoria['itens']:
                if item['nome'].lower() == nome.lower():
                    categoria['itens'].remove(item)
                    print(f"{nome} foi removido.")
                    return
    print(f"{nome} não foi encontrado.")

def limpar_cardapio(cardapio):
    cardapio.clear()
    print("Cardápio foi limpo com sucesso.")
