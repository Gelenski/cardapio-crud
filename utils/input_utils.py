from utils.cardapio import carregar_cardapio
from config.config import CAMINHO_CARDAPIO

cardapio, _, _ = carregar_cardapio(CAMINHO_CARDAPIO)

def testa_string_dicionario(string, dicionario):
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
