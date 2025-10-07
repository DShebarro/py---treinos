conjunto = set() # conjunto vazio

# Adicionando elementos ao conjunto
conjunto.add(10) 
conjunto.add(20) 

print("Conjunto após adicionar elementos: ", conjunto)

# Verificando se o elemento está no conjunto

elemento = 20
if elemento in conjunto:
    print("O elemento {} está no conjunto.".format(elemento))
else:
    print("O elemento {} não está no conjunto.".format(elemento))

# Removendo o elemento

conjunto.remove(20)

print("Conjunto após remover o elemento: ", conjunto)