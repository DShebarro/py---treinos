# FUNÇÂO FILTER

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
numeros_impares = list(filter(lambda x: x % 2 != 0, numeros))
print("Os números pares são: {}".format(numeros_pares))
print("Os números ímpares são: {}".format(numeros_impares))