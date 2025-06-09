from utils.cardapio import carregar_cardapio
from config.config import CAMINHO_CARDAPIO

lista = []

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

if __name__ == "__main__":
    selecionar_itens()
