
def contagem_palavras (string):
    dicionario = {}
    palavras = string.split(" ")
    for palavra in palavras:
        if palavra in dicionario:
            dicionario[palavra] += 1
        else:
            dicionario[palavra] = 1
    return dicionario