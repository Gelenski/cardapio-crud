def captura_nome_restaurante():
    """Captura o nome do restaurante"""
    while True:
        nome = input("Digite o nome do restaurante: ")
        if nome == "":
            print("O nome do restaurante não pode ser vazio.")
        else:
            return nome

def captura_porcentagem_garcom():
    """Captura a porcentagem do garçom"""
    while True:
        porcentagem = input("Digite a porcentagem dos garçons do restaurante: ")
        if porcentagem.replace(".", "", 1).isdigit():
            return float(porcentagem)
        else:
            print("Digite um número válido.")