

def contagem_frequencia(strings):
    dicionario = {}
    for string in strings:
        if string in dicionario:
            dicionario[string] += 1
        else:
            dicionario[string] = 1
    return dicionario
