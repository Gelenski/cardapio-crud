from config import carregar_cardapio, salvar_cardapio, captura_nome_restaurante, captura_porcentagem_garcom

CAMINHO_CARDAPIO = "cardapio.txt"

CATEGORIAS_DISPONIVEIS = ["entradas", "pratos_principais", "sobremesas", "bebidas"]

def mostrar_categorias():
    print("\nCategorias disponíveis:")
    for idx, cat in enumerate(CATEGORIAS_DISPONIVEIS, start=1):
        print(f"{idx}. {cat.replace('_', ' ').capitalize()}")

def selecionar_categoria():
    mostrar_categorias()
    try:
        escolha = int(input("Digite o número da categoria: "))
        if 1 <= escolha <= len(CATEGORIAS_DISPONIVEIS):
            return CATEGORIAS_DISPONIVEIS[escolha - 1]
        else:
            print("Número inválido.")
            return None
    except:
        print("Entrada inválida. Digite um número.")
        return None

def ver_cardapio(cardapio):
    if not cardapio:
        print("\nCardápio vazio no momento.")
        return
    for categoria in cardapio:
        print(f"\n{categoria['categoria'].capitalize()}:")
        for item in categoria['itens']:
            print(f"• {item['nome']} - R${item['preco']:.2f}")

def editar_item(cardapio):
    tipo = selecionar_categoria()
    if not tipo:
        return

    for categoria in cardapio:
        if categoria['categoria'].lower() == tipo.lower():
            if not categoria['itens']:
                print(f"\nA categoria '{tipo}' está vazia.")
                return
            print(f"\nItens da categoria '{tipo}':")
            for item in categoria['itens']:
                print(f"• {item['nome']} - R${item['preco']:.2f}")
            break
    else:
        print(f"A categoria '{tipo}' está vazia")
        return

    nome = input(f"\nDigite o nome do item que deseja editar: ").strip()
    if not nome:
        print("Nome não pode estar em branco.")
        return

    for item in categoria['itens']:
        if item['nome'].lower() == nome.lower():
            print(f"Item encontrado: {item['nome']} - R${item['preco']:.2f}")
            novo_nome = input("Novo nome (Enter para manter): ").strip() or item['nome']
            try:
                novo_preco = input("Novo preço (Enter para manter): ").strip()
                item['preco'] = float(novo_preco.replace(",", ".")) if novo_preco else item['preco']
            except:
                print("Preço inválido. Mantido o preço anterior.")
            item['nome'] = novo_nome
            print("Item atualizado com sucesso.")
            return

    print(f"O item '{nome}' não foi encontrado na categoria '{tipo}'.")



def incluir_item(cardapio):
    tipo = selecionar_categoria()
    if not tipo:
        return
    nome = input(f"Nome do item a adicionar na categoria '{tipo}': ").strip()
    if not nome:
        print("Nome não pode estar em branco.")
        return
    try:
        preco = float(input(f"Preço do {nome}: R$ ").replace(",", "."))
        for categoria in cardapio:
            if categoria['categoria'].lower() == tipo.lower():
                categoria['itens'].append({"nome": nome, "preco": preco})
                break
        else:
            cardapio.append({"categoria": tipo, "itens": [{"nome": nome, "preco": preco}]})
        print(f"{nome} foi incluído no cardápio.")
    except:
        print("Preço inválido. Use apenas números.")

def excluir_item(cardapio):
    tipo = selecionar_categoria()
    if not tipo:
        return
    for categoria in cardapio:
        if categoria['categoria'].lower() == tipo.lower():
            if not categoria['itens']:
                print(f"A categoria '{tipo}' está vazia.")
                return
            print(f"\nItens da categoria '{tipo}':")
            for item in categoria['itens']:
                print(f"• {item['nome']} - R${item['preco']:.2f}")
            break
    else:
        print(f"A categoria '{tipo}' não foi encontrada.")
        return
    nome = input(f"Nome do item a remover da categoria '{tipo}': ").strip()
    if not nome:
        print("Nome não pode estar em branco.")
        return
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

    #TODO: Implementar na def main --------------------------------

def buscar_item(item):
    cardapio, _, _ = carregar_cardapio(CAMINHO_CARDAPIO)
    for categoria in cardapio:
        for comida in categoria["itens"]:
            if comida["nome"].lower() == item.lower():
                print(f"O item: {comida['nome']} está contido no cardápio.")
                return True
    print("O item digitado não está contido no cardápio.")
    return False

        
def imprimir_itens():
    cardapio, _, _ = carregar_cardapio(CAMINHO_CARDAPIO)
    lista = []
    contador = 1
    for categoria in cardapio:
        print(f"\n{categoria['categoria'].capitalize()}:")
        for item in categoria['itens']:
            nome = item['nome'].replace("-", "")
            preco = item['preco']
            print(f"{contador}. {nome} - R${preco:.2f}")
            lista.append({"indice": contador, "nome": nome, "preco": preco})
            contador += 1
    return lista

def selecionar_itens():
    lista = imprimir_itens()
    if lista:
        valores = []
        escolha = input("\nDigite os números dos itens que deseja (separados por vírgula): ").split(',')
        for e in escolha:
            try:
                indice = int(e.strip())
                for i in lista:
                    if i['indice'] == indice:
                        print(f"- {i['nome']} - R${i['preco']:.2f}")
                        valores.append(i['preco'])
            except:
                print(f"Entrada inválida: {e}")
        print(f"\nValor total: R${sum(valores):.2f}")
    else:
        print('\nO cardápio está vazio.')

def main():
    cardapio, nome_restaurante, porcentagem_garcom = carregar_cardapio(CAMINHO_CARDAPIO)

    if not cardapio:
        cardapio = []

    if not nome_restaurante:
        nome_restaurante = captura_nome_restaurante()

    if not porcentagem_garcom:
        porcentagem_garcom = captura_porcentagem_garcom()

    while True:
        print("\n-------- OPÇÕES DISPONÍVEIS --------\n")
        print("1. Ver Cardápio")
        print("2. Incluir item")
        print("3. Excluir item")
        print("4. Limpar o cardápio")
        print("5. Buscar item")
        print("6. Alterar item")
        print("7. Fechar caixa")
        print("8. Encerrar e salvar o cardápio")

        opcao = input("Selecione uma das opções: ")
        if opcao == "1":
            ver_cardapio(cardapio)
        elif opcao == "2":
            incluir_item(cardapio)
        elif opcao == "3":
            excluir_item(cardapio)
        elif opcao == "4":
            limpar_cardapio(cardapio)
        elif opcao == "5":
            nome_item = input("Digite o nome do item que deseja buscar: ").strip()
            salvar_cardapio(cardapio, CAMINHO_CARDAPIO, nome_restaurante, porcentagem_garcom)
            buscar_item(nome_item)
        elif opcao == "6":
            salvar_cardapio(cardapio, CAMINHO_CARDAPIO, nome_restaurante, porcentagem_garcom)
            editar_item(cardapio)
        elif opcao == "7":
            salvar_cardapio(cardapio, CAMINHO_CARDAPIO, nome_restaurante, porcentagem_garcom)
            selecionar_itens()
        elif opcao == "8":
            print("Fechando cardápio.")
            salvar_cardapio(cardapio, CAMINHO_CARDAPIO, nome_restaurante, porcentagem_garcom)
            break
        else:
            print("Escolha inválida, digite uma opção válida.")


if __name__ == "__main__":
    main()
