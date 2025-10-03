# FUNÇÂO MAP
precos_em_dolares = [100, 50, 75, 120, 300]
taxa_de_cambio = 5.32
precos_em_reais = list(map(lambda x: x * taxa_de_cambio, precos_em_dolares))
print("O valor em reais é: R$ {}".format(precos_em_reais))