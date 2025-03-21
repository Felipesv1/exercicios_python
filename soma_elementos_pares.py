
def soma_elementos_pares (lista):
    soma = 0;
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            soma += lista[i]
    return soma