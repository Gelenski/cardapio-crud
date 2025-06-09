from config.config import CAMINHO_CARDAPIO
from config.settings import captura_nome_restaurante, captura_porcentagem_garcom
from ui.interface import visualizar_menu, ver_cardapio, incluir_item, excluir_item, limpar_cardapio
from utils.cardapio import salvar_cardapio, carregar_cardapio

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