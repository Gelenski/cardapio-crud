def testa_string_dicionario(string, dicionario):
    """Teste se a string não é vazia e se está contida no dicionário(cardapio)"""
    if not string:
        return False
    for categoria in dicionario:
        if string in categoria['categoria']:
            return True
        for item in categoria['itens']:
            if string in item['nome']:
                return True
    return False
