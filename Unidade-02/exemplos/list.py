# cores = ["Azul", "Preto", "Amarelo", "Vermelho", "Rosa"]
# for cor in cores:
#     print("Posição = {}, cor {}".format(cores.index(cor), cor))

linguagens = ["Python", "Java", "JavaScript", "C", "#C++", "C#" "PHP", "Ruby", "Go", "Swift"]
print ("Antes da listcomp = ", linguagens)
linguagens = [item.lower() for item in linguagens] #Criando uma nova lista
print ("\nDepois da listcomp = ", linguagens)