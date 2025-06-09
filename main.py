CAMINHO_CARDAPIO = "cardapio.txt"

def salvar_cardapio(cardapio, caminho, nome_restaurante, porcentagem_garcom):
    with open(caminho, "w", encoding="utf-8") as arquivo:
        arquivo.write(f"@NOME_RESTAURANTE: {nome_restaurante}\n")
        arquivo.write(f"@PORCENTAGEM_GARCOM: {porcentagem_garcom}\n")
        for categoria in cardapio:
            arquivo.write(f"Categoria: {categoria['categoria']}\n")
            for item in categoria['itens']:
                arquivo.write(f"-{item['nome']}-R${item['preco']}\n")

def carregar_cardapio(caminho):
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            cardapio = []
            nome_restaurante = ""
            porcentagem_garcom = 0.0
            categoria_atual = None
            for linha in arquivo:
                linha = linha.strip()
                if linha:
                    if linha.startswith("@NOME_RESTAURANTE:"):
                        nome_restaurante = linha.split(": ", 1)[1].strip()
                    elif linha.startswith("@PORCENTAGEM_GARCOM:"):
                        porcentagem_garcom = float(linha.split(": ", 1)[1].strip())
                    elif linha.startswith("Categoria:"):
                        if categoria_atual:
                            cardapio.append(categoria_atual)
                        nome_categoria = linha.split("Categoria:", 1)[1].strip()
                        categoria_atual = {"categoria": nome_categoria, "itens": []}
                    elif linha.startswith("-"):
                        nome_item, preco = linha.rsplit("-R$", 1)
                        preco = float(preco)
                        categoria_atual["itens"].append({"nome": nome_item.strip("- "), "preco": preco})
            if categoria_atual:
                cardapio.append(categoria_atual)
            return cardapio, nome_restaurante, porcentagem_garcom
    except:
        print("Cardápio não encontrado, criando um novo.")
        salvar_cardapio([], caminho, "", 0.0)
        return [], "", 0.0
    

def captura_nome_restaurante():
    """Captura o nome do restaurante"""
    while True:
        nome = input("Digite o nome do restaurante: ")
        if nome == "":
            print("O nome do restaurante não pode ser vazio.")
        else:
            return nome

def captura_porcentagem_garcom():
    """Captura a porcentagem do garçom"""
    while True:
        porcentagem = input("Digite a porcentagem dos garçons do restaurante: ")
        if porcentagem.replace(".", "", 1).isdigit():
            return float(porcentagem)
        else:
            print("Digite um número válido.")


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

def imprimir_itens():
    cardapio, _, _ = carregar_cardapio(CAMINHO_CARDAPIO)
    contador = 0
    for categoria in cardapio:
        print(f"\n{categoria['categoria'].capitalize()}:")
        for item in categoria['itens']:
            nome = item['nome'].replace("-", "")
            preco = item['preco']
            print(f"{contador}. {nome} - R${preco:.2f}")
            lista.append({"indice": contador, "nome": nome, "preco": preco})
            contador += 1

def selecionar_itens():
    imprimir_itens()
    valores = []
    escolha = input("\nDigite os números dos itens que deseja (separados por vírgula): ").split(',')
    for e in escolha:
        try:
            indice = int(e.strip())
            for i in lista:
                if i['indice'] == indice:
                    print(f"- {i['nome']} - R${i['preco']:.2f}")
                    valores.append(i['preco'])
        except ValueError:
            print(f"Entrada inválida: {e}")
    print(f"\nValor total: R${sum(valores):.2f}")


def main():
    cardapio, nome_restaurante, porcentagem_garcom = carregar_cardapio(CAMINHO_CARDAPIO)

    if not cardapio:
        print("Nenhum cardápio encontrado. Criando um novo.")
        cardapio = []

    if not nome_restaurante:
        nome_restaurante = captura_nome_restaurante()

    if not porcentagem_garcom:
        porcentagem_garcom = captura_porcentagem_garcom()

    while True:
        visualizar_menu()
        opcao = input("Selecione uma das opções: ")
        if opcao == "1":
            ver_cardapio(cardapio)
        elif opcao == "2":
            tipo = input("Categoria (entradas, pratos_principais, sobremesas, bebidas): ")
            incluir_item(cardapio, tipo)
        elif opcao == "3":
            tipo = input("Categoria para excluir item (entradas, pratos_principais, sobremesas, bebidas): ")
            excluir_item(cardapio, tipo)
        elif opcao == "6":
            limpar_cardapio(cardapio)
        elif opcao == "7":
            print("Fechando cardápio.")
            salvar_cardapio(cardapio, CAMINHO_CARDAPIO, nome_restaurante, porcentagem_garcom)
            break
        else:
            print("Escolha inválida. Tente novamente.")

if __name__ == "__main__":
    main()