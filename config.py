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
        nome_restaurante = input("Digite o nome do restaurante: \n")
        if nome_restaurante == "":
            print("O nome do restaurante não pode ser vazio, digite novamente.")
        else:
            return nome_restaurante

def captura_porcentagem_garcom():
    """Captura a porcentagem do garçom"""
    while True:
        porcentagem_garcom = input("Digite a porcentagem dos garçons do restaurante: \n")
        if porcentagem_garcom.replace(".", "", 1).isdigit():
            return float(porcentagem_garcom)
        else:
            print("Digite um número válido.")