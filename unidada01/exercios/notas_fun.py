# Lista de notas dos estudantes
notas =[7.5, 8.0, 5.5, 9.0, 5.5]

# função de média
def calcular_media(notas):
    total = sum(notas)
    media = total / len(notas)
    return media

# FUNÇÃO LAMBDA DE ARRENDONDAMENTO
arredondar_media = lambda media: round(media, 2)

# Calcular media
media = calcular_media(notas)
media_arredondada = arredondar_media(media)

# Verificar situaçõa do estudante
situacao = "Aprovado" if media_arredondada >= 7 else "Reprovado"

# if media_arredondada >= 7.0:
#     print("Aprovado")
# else:
#     print("Reprovado")

# Resultado
print("Notas de estudante: {}".format(notas))
print("Média dos estudantes: {}".format(media_arredondada))
print("Situação do estudante: {}".format(situacao))