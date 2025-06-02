from cardapio import *

lista = []

def imprimir_itens():
    cardapio = carregar_cardapio(caminho_cardapio)
    contador = 0
    for categoria in cardapio:
       print()
       print(f'{categoria['categoria']}')
       for item in categoria['itens']:
           nome = item['nome'].replace("-", "")
           preco = item['preco']
           print(f'{contador}. {nome} - R${item['preco']}')
           item_indice = {"indice": contador, "nome": nome, 'preco': preco}
           lista.append(item_indice)
           contador+=1

def selecionar_itens():
    imprimir_itens()
    valores = []
    escolha = input('\nDigite os números dos itens que deseja (separados por vírgula): ').split(',')
    for e in escolha:
        indice = int(e.strip())
        for i in lista:
            if i['indice'] == indice:
                print(f"- {i['nome']} - R${i['preco']}")
                valores.append(i['preco'])
    print()           
    print(f'O valor total é: R${sum(valores)}')

selecionar_itens()