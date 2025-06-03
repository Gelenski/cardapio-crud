def salvar_cardapio(cardapio, caminho, nome_restaurante, porcentagem_garcom):
    """Salva o cardápio em um arquivo de texto com no formato de lista de dicionários"""
    with open(caminho, "w", encoding="utf-8") as arquivo:
        arquivo.write(f"@NOME_RESTAURANTE: {nome_restaurante}\n")
        arquivo.write(f"@PORCENTAGEM_GARCOM: {porcentagem_garcom}\n")
        for categoria in cardapio:
            arquivo.write(f"Categoria: {categoria['categoria']}\n")
            for item in categoria['itens']:
                arquivo.write(f"-{item['nome']}-R${item['preco']}\n")

def carregar_cardapio(caminho):
    """Carrega o cardápio de um arquivo de texto e retorna uma lista de dicionários"""    
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            cardapio = []
            categoria_atual = None
            for linha in arquivo:
                linha = linha.strip()
                if linha:
                    if not linha.startswith("-") and linha.startswith("Categoria:"):
                        if categoria_atual:
                            cardapio.append(categoria_atual)
                        categoria_atual = {"categoria": linha, "itens": []}
                    elif linha.startswith("@NOME_RESTAURANTE:"):
                        nome_restaurante = linha.split(": ", 1)[1].strip()
                        
                    elif linha.startswith("@PORCENTAGEM_GARCOM:"):
                        porcentagem_garcom = linha.split(": ", 1)[1].strip()

                    else:
                        nome_item, preco = linha.rsplit("-R$", 1)
                        # Atribui float para que seja somado posteriormente
                        preco = float(preco)
                        categoria_atual["itens"].append({"nome": nome_item.strip(), "preco": preco})
            if categoria_atual:
                cardapio.append(categoria_atual)
            return cardapio, nome_restaurante, porcentagem_garcom
        # Retorna o cardápio com índice 0, nome do restaurante com índice 1 e porcentagem do garçom com índice 2
    except:
        print("Cardápio não encontrado, criando um novo.")
        return []
