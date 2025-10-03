for numero in range (1, 11):
    if numero % 2 == 0:
        print("O primeiro número encontrado é: ", numero)
        break # Uma condição de parada 

for numero in range (1, 11):
    if numero == 5:
        continue # Uma condição que pula quando encontra o valor
    print(numero)