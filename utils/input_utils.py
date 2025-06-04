from cardapio import carregar_cardapio, caminho_cardapio

cardapio = carregar_cardapio(caminho_cardapio)

def testa_string_dicionario(string, dicionario):
    """Verifica se a string está contida em alguma categoria ou nome de item"""
    if not string:
        return False
    for categoria in dicionario:
        if string.lower() in categoria['categoria'].lower():
            return True
        for item in categoria['itens']:
            if string.lower() in item['nome'].lower():
                return True
    return False

entrada_usuario = input("Digite o nome de um item ou categoria para buscar no cardápio: ")

if testa_string_dicionario(entrada_usuario, cardapio):
    print(f"'{entrada_usuario}' está no cardápio!")
else:
    print(f"'{entrada_usuario}' não foi encontrado no cardápio.")