filmes = ["Filme 1", "Filme 2", "Filme 3", "Filme 4", "Filme 5"]

print("Bem-Vindo à classificação de filmes!")
print("Você tem cinco filmes para classificar.")
print("Digite '0' a qualquer momento para parar.\n")

for filme in filmes:
    classificacao = input("Como você classificaria {} de 1 a 5 (ou 0 para sair): ".format(filme))
    if classificacao == "0":
        print("Classificação interropida!")
        break

    classificacao = int(classificacao)
    if classificacao < 1 or classificacao > 5:
        print("Use um valor de classificação válido de 1 a 5!!")
    else: 
        print("Você classificou {} com {} estrelas\n")