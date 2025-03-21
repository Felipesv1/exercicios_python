
def combina_dicionarios(primerio_dicionario, segundo_dicionario):
    dicionario_somado = {}
    
    dicionario_somado.update(primerio_dicionario)
    dicionario_somado.update(segundo_dicionario)
    for d1 in primerio_dicionario:
        for d2 in segundo_dicionario:
            if d1 == d2:
                dicionario_somado[d1] += primerio_dicionario[d2]
    return dicionario_somado

print(combina_dicionarios(d1, d2))