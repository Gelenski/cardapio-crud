caminho_cardapio = "cardapio.txt"

def salvar_cardapio(cardapio, caminho):
    """Salva o cardápio em um arquivo de texto com no formato de lista de dicionários"""
    with open(caminho, "w", encoding="utf-8") as arquivo:
        for categoria in cardapio:
            arquivo.write(f"Categoria: {categoria['categoria']}\n")
            for item in categoria['itens']:
                arquivo.write(f"    -{item['nome']}-R${item['preco']:.2f}\n")

def carregar_cardapio(caminho):
    """Carrega o cardápio de um arquivo de texto e retorna uma lista de dicionários"""
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            cardapio = []
            categoria_atual = None
            for linha in arquivo:
                linha = linha.strip()
                if linha:
                    if not linha.startswith("-"):
                        if categoria_atual:
                            cardapio.append(categoria_atual)
                        categoria_atual = {"categoria": linha, "itens": []}
                    else:
                        nome_item, preco = linha.rsplit("-R$", 1)
                        # Atribui float para que seja somado posteriormente
                        preco = float(preco)
                        categoria_atual["itens"].append({"nome": nome_item.strip(), "preco": preco})
            if categoria_atual:
                cardapio.append(categoria_atual)
            return cardapio
    except:
        print("Cardápio não encontrado, criando um novo.")
        return []

salvar_cardapio([
    {
        "categoria": "Bebidas",
        "itens": [
            {"nome": "Refrigerante", "preco": 5.00},
            {"nome": "Suco", "preco": 5.00}
        ]
    },
    {
        "categoria": "Entradas",
        "itens": [
            {"nome": "Salada", "preco": 5.00},
            {"nome": "Sopa", "preco": 5.00}
        ]
    },
    {
        "categoria": "Pratos Principais",
        "itens": [
            {"nome": "Pizza", "preco": 5.00},
            {"nome": "Hambúrguer", "preco": 5.00}
        ]
    },
    {
        "categoria": "Sobremesas",
        "itens": [
            {"nome": "Bolo", "preco": 5.00},
            {"nome": "Sorvete", "preco": 5.00}
        ]
    }
], caminho_cardapio)
