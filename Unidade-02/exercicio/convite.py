convidados = ["Davy", "Brendson", "Larissa", "Marcelo", "Jehu"]

confirmados = ["Davy", "Larissa"]

nao_confirmado = [convidado for convidado in convidados if convidado not in confirmados]
print("Convidados que ainda não confirmados:\n")
for pessoa in nao_confirmado:
    print(pessoa)

print("\nEnviar lembretes para os convidados que ainda não confirmaram!!")