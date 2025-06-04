from config.settings import captura_nome_restaurante, captura_porcentagem_garcom
from ui.interface import visualizar_menu, ver_cardapio, incluir_prato, excluir_prato, incluir_bebida, excluir_bebida, limpar_cardapio
from utils.cardapio import salvar_cardapio, carregar_cardapio

caminho_cardapio = "cardapio.txt"

def main():
    # Parte de configuração
    cardapio, nome_restaurante, porcentagem_garcom = carregar_cardapio(caminho_cardapio)

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
            ver_cardapio()
        elif opcao == "2":
            tipo = input("Deseja incluir (1) Comida ou (2) Bebida? ")
            if tipo == "1": 
                incluir_prato()
            elif tipo == "2":
                incluir_bebida()
            else:
                print("Opção inválida.")
        elif opcao == "3":
            tipo = input("Deseja excluir (1) Comida ou (2) Bebida? ")
            if tipo == "1":
                excluir_prato()
            elif tipo == "2":
                excluir_bebida()
            else:
                print("Opção inválida.")
        elif opcao == "6":
            limpar_cardapio()
        elif opcao == "7":
            print("Fechando cardápio.")
            salvar_cardapio(cardapio, caminho_cardapio, nome_restaurante, porcentagem_garcom)
            break
        else:
            print("Escolha inválida. Tente novamente.")


main()