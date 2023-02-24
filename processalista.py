def maior_impar(lista):
    numero_impar = []
    for numero in lista:
        if (numero % 2 != 0):
            numero_impar.append(numero)
    maior_numero = max(numero_impar)
    return maior_numero


def menor_impar(lista):
    numero_impar = []
    for numero in lista:
        if (numero % 2 != 0):
            numero_impar.append(numero)
    menor_numero = min(numero_impar)
    return menor_numero
