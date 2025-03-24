lista_numeros = [1, 3, 3, 2, 1, 1, 4, 4, 4, 2, 2, 2, 5, 5]

def retorna_tres_numeros_mais_frequentes_na_lista(lista):
    
    frequencias = {}

    for num in lista:
        if num in frequencias:
            frequencias[num] += 1
        else:
            frequencias[num] = 1


    mais_frequentes = sorted(frequencias, key=frequencias.get, reverse=True)[:3]

    return mais_frequentes

print(retorna_tres_numeros_mais_frequentes_na_lista(lista_numeros))