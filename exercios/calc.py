# Solicita a usuário que insira o valor do produto e o percentual de desconto
valor_produto = float(input("Digite o valor do produto: "))
percentual_desconto = float(input("Digite o percentual de desconto: "))

if percentual_desconto < 0 or percentual_desconto > 100:
    print ("ERRO!! - O percentual de desconto deve estar entre 0 e 100.")
else:
    desconto = valor_produto * (percentual_desconto / 100)

valor_final = valor_produto - desconto

print("O valor do produto: {:.2f}".format(valor_final))
