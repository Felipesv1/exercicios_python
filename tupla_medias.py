
def calcula_a_media_das_notas_e_transforma_em_tupla(dicionario):
    
    lista_de_tuplas = []
    for chave, values in dicionario.items():
        dicionario[chave] = round(sum(values) / 3, 2)
    lista_de_tuplas = list(dicionario.items())
    return lista_de_tuplas

