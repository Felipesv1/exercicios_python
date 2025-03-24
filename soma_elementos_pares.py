
def soma_elementos_pares (lista):
    soma = 0;
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            soma += lista[i]
    return soma

lista = [1, 4, 10, 6, 3, 7, 9]

print(f'A soma dos pares na lista é:{soma_elementos_pares(lista)}')