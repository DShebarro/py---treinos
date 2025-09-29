# def soma (a, b):
#     resultado = a + b
#     return resultado

# resultado_soma = soma (10, 7)
# print("O resultado da soma é:", resultado_soma)

def e_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
    
numero = 7474747
if e_par(numero):
    print(f"{numero} é par")
else:
    print(f"{numero} é ímpar")